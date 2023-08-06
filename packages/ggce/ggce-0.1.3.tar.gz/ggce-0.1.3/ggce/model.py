from copy import deepcopy, copy
import numpy as np
import math

from monty.json import MSONable

from ggce.logger import logger


def model_coupling_map(coupling_type, t, Omega, lam):
    """Returns the value for g, the scalar that multiplies the coupling in the
    Hamiltonian. Converts the user-input lambda value to this g. Uses
    pre-defined values for the dimensionless coupling to get g for a variety
    of pre-defined default models.

    Parameters
    ----------
    coupling_type : str
        The desired coupling type. Can be Holstein, Peierls, BondPeierls, or
        EdwardsFermionBoson.
    t : float
        The hopping strength.
    Omega : float
        The (Einstein) phonon frequency. Absolute value is taken, since it will
        be negative sometimes (in the case of TFD).
    lam : float
        The dimensionless coupling.

    Returns
    -------
    float
        The value for the coupling (g).

    Raises
    ------
    RuntimeError
        If an unknown coupling type is provided.
    """

    if coupling_type == "Holstein":
        return math.sqrt(2.0 * t * np.abs(Omega) * lam)
    elif coupling_type == "EdwardsFermionBoson":
        return lam
    elif coupling_type == "Peierls":
        return math.sqrt(t * np.abs(Omega) * lam / 2.0)
    elif coupling_type == "BondPeierls":
        return math.sqrt(t * np.abs(Omega) * lam)
    else:
        raise RuntimeError


class SingleTerm(MSONable):
    """Contains the shift indexes, dagger status, coupling strength and boson
    type of a single term. Particularly, this single term corresponds to
    a single element of the sum in equation (10) in this
    `PRB <https://journals.aps.org/prb/abstract/10.1103/
    PhysRevB.104.035106>`_,

    .. math::

        g \\sum_i c_i^\\dagger c_{i + \\psi} b^d_{i + \\phi}
    """

    @property
    def psi(self):
        """The shift term on :math:`c`.

        Returns
        -------
        numpy.array
        """

        return self._psi.copy()

    @psi.setter
    def psi(self, x):
        if not isinstance(x, np.ndarray):
            logger.critical(f"psi {x} must be of type numpy.array")
        self._psi = x

    @property
    def phi(self):
        """The shift term on :math:`b^d`.

        Returns
        -------
        numpy.array
        """

        return self._phi.copy()

    @phi.setter
    def phi(self, x):
        if not isinstance(x, np.ndarray):
            logger.critical(f"phi {x} must be of type numpy.array")
        self._phi = x

    @property
    def dag(self):
        """The "dagger status" of the term. "+" for creation operator and "-"
        for annihilation operator. Must be either "+" or "-".

        Returns
        -------
        str
        """

        return self._dag

    @dag.setter
    def dag(self, x):
        if x not in ["+", "-"]:
            raise logger.critical(f"Invalid choice for dag: {x}")
        self._dag = x

    @property
    def coupling(self):
        """The coupling strength of the term. Directly multiplies the operators
        in the Hamiltonian. This is :math:`g`.

        Returns
        -------
        float
        """

        return self._coupling

    @coupling.setter
    def coupling(self, x):
        if not isinstance(x, (int, float)):
            raise logger.critical(f"Coupling {x} must be int or float")
        self._coupling = x

    @property
    def phonon_index(self):
        """The index of the phonon provided.

        Returns
        -------
        int
        """

        return self._phonon_index

    @phonon_index.setter
    def phonon_index(self, x):
        if not isinstance(x, int):
            raise logger.critical(f"Phonon index {x} must be of type int")
        if x < 0:
            raise logger.critical(f"Phonon index {x} must be >= 0")
        self._phonon_index = x

    @property
    def phonon_frequency(self):
        """The frequency of the phonon provided.

        .. note::

            The ``phonon_frequency`` can be negative in the TFD formalism.

        Returns
        -------
        float
            Description
        """

        return self._phonon_frequency

    @phonon_frequency.setter
    def phonon_frequency(self, x):
        if not isinstance(x, (int, float)):
            raise logger.critical(f"Phonon frequency {x} must be int or float")
        self._phonon_frequency = x

    def __init__(
        self,
        coupling_type,
        psi,
        phi,
        dag,
        coupling,
        phonon_index,
        phonon_frequency,
    ):
        """Initializes the SingleTerm class."""

        self._coupling_type = coupling_type
        self.psi = psi
        self.phi = phi
        self.dag = dag
        self.coupling = coupling
        self.phonon_index = phonon_index
        self.phonon_frequency = phonon_frequency

    def __str__(self):
        return (
            f"{self._coupling_type}: {self.coupling:.02f} x ({self.psi} "
            f"{self.phi} {self.dag}) | {self.phonon_index} "
            f"({self.phonon_frequency:.02f})"
        )

    def __repr__(self):
        return self.__str__()


class Hamiltonian(MSONable):
    """Container for all relevant parameters for defining the Hamiltonian.
    Current available are `Holstein`, `EdwardsFermionBoson`, `BondPeierls`,
    and `Peierls`."""

    # Old x is now psi
    # Old y is now phi
    # Old d is now dag
    # Old g is now sign; g must be provided elsewhere
    # Same as the PRB!

    @property
    def terms(self):
        return self._terms

    @property
    def phonon_frequencies(self):
        return self._phonon_frequencies

    @property
    def dimension(self):
        return self._dimension

    def get_dict_rep(self):
        """Provides a dictionary representation of the Hamiltonian. Packages
        terms by the phonon type.

        Returns
        -------
        dict
        """

        d = dict()
        for term in self._terms:
            try:
                d[term.phonon_index].append(term)
            except KeyError:
                d[term.phonon_index] = [term]
        return d

    def _get_SingleTerm_objects(
        self, coupling_type, coupling_strength, phonon_index, phonon_frequency
    ):
        """Gets the SingleTerm objects corresponding to some coupling_type,
        coupling strength and phonon_index."""

        # Holstein is easy. In all dimensions, it "looks" the same.
        if coupling_type == "Holstein":
            return [
                SingleTerm(
                    coupling_type,
                    np.array([0] * self._dimension),
                    np.array([0] * self._dimension),
                    "+",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([0] * self._dimension),
                    np.array([0] * self._dimension),
                    "-",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
            ]

        elif coupling_type == "EdwardsFermionBoson":
            return [
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([1]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([-1]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([0]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([0]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
            ]

        elif coupling_type == "BondPeierls":
            return [
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([0.5]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([0.5]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([-0.5]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([-0.5]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
            ]

        elif coupling_type == "Peierls":
            return [
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([0]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([0]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([1]),
                    "+",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([1]),
                    np.array([1]),
                    "-",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([-1]),
                    "+",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([-1]),
                    "-",
                    coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([0]),
                    "+",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
                SingleTerm(
                    coupling_type,
                    np.array([-1]),
                    np.array([0]),
                    "-",
                    -coupling_strength,
                    phonon_index,
                    phonon_frequency,
                ),
            ]

        raise RuntimeError(f"Unknown coupling type {coupling_type}")

    def __init__(
        self, terms=[], phonon_frequencies=[], dimension=1, hopping=1.0
    ):
        """Sets the list of terms as an empty list"""

        self._terms = deepcopy(terms)
        self._phonon_frequencies = copy(phonon_frequencies)
        self._dimension = dimension
        self._hopping = hopping

    def _add_(
        self,
        coupling_type,
        phonon_index,
        phonon_frequency,
        coupling_strength=None,
        dimensionless_coupling_strength=None,
        coupling_multiplier=1.0,
    ):
        """Helper method for adding a term to the attribute. See `add_` for
        more details."""

        # XOR -- this should be taken care of outside this func
        c1 = coupling_strength is not None
        c2 = dimensionless_coupling_strength is not None
        if not c1 ^ c2:
            raise ValueError("Coupling strength errors")

        if c2:
            try:
                g = model_coupling_map(
                    coupling_type,
                    self._hopping,
                    phonon_frequency,
                    dimensionless_coupling_strength,
                )
            except RuntimeError:
                logger.error(f"Unknown coupling type {coupling_type}")
                return
        else:
            g = coupling_strength
        assert g is not None

        try:
            terms = self._get_SingleTerm_objects(
                coupling_type,
                g * coupling_multiplier,
                phonon_index,
                phonon_frequency,
            )
        except RuntimeError:
            logger.error(f"Unknown coupling type {coupling_type}")
            return

        if phonon_frequency not in self._phonon_frequencies:
            self._phonon_frequencies.append(phonon_frequency)

        self._terms.extend(terms)

    def add_(
        self,
        coupling_type,
        phonon_index,
        phonon_frequency,
        coupling_strength=None,
        dimensionless_coupling_strength=None,
        coupling_multiplier=1.0,
    ):
        """Adds a set of terms to the list of terms, corresponding to the
        provided coupling type, strength and index.

        Parameters
        ----------
        coupling_type : str
            The type of coupling to add to the Hamiltonian.
        phonon_index : int
            The index of the phonon to register.
        phonon_frequency : float
            The Einstein phonon frequency corresponding to the phonon creation
            and annihilation operators. Traditionally denoted :math:`\\Omega`.
        coupling_strength : float
            The strength of the coupling to add. This is g. Default is None.
            If None, requires `dimensionless_coupling_strength` to be set.
        dimensionless_coupling_strength : float
            The dimensionless coupling strength, which is a function of the
            hopping, and phonon frequency, as well as the type of model.
            Default is None. If None, requires `coupling_strength` to be set.
        coupling_multiplier : float, optional
            Extra term which will multiply the coupling. This could be a
            prefactor from e.g. the TFD formalism. Default is 1.0
        """

        args = {key: value for key, value in locals().items() if key != "self"}
        self._add_(
            coupling_type,
            phonon_index,
            phonon_frequency,
            coupling_strength,
            dimensionless_coupling_strength,
            coupling_multiplier,
        )
        logger.debug(f"Added {args}")

    def __str__(self):
        xx = "\n".join([str(xx) for xx in self._terms])
        return xx.replace(r"\n", "\n")

    def __repr__(self):
        return self.__str__()

    def visualize(self):
        print(self.__str__())


class Model(MSONable):
    """The Model object. Contains all information to be fed to the System
    class for solving for the Green's function.

    .. warning::

        Note it is highly recommended to use the :class:`from_parameters`
        classmethod instead, since the constructor is primarily designed to be
        used with MSONable and not all parameters are intended to be manually
        modified.
    """

    @property
    def temperature(self):
        """The temperature for a TFD simulation, if requested (the default is
        0.0).

        Returns
        -------
        float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, x):
        if not isinstance(x, (float, int)):
            logger.error(f"Temperature {x} must be a number")
            return
        if x < 0.0:
            logger.error(f"Temperature {x} must be non-negative")
            return
        self._temperature = x

    @property
    def hopping(self):
        """The nearest-neighbor hopping term (the default is 1.0).

        Returns
        -------
        float
        """

        return self._hamiltonian._hopping

    @property
    def lattice_constant(self):
        """The lattice constant (the default is 1.0).

        Returns
        -------
        float
        """

        return self._lattice_constant

    @lattice_constant.setter
    def lattice_constant(self, x):
        if not isinstance(x, (float, int)):
            logger.error(f"Lattice constant {x} must be a number")
            return
        if x <= 0.0:
            logger.error(f"Lattice constant {x} must be positive")
            return
        if x != 1.0:
            logger.warning(f"Lattice constant {x}!=1, which is unusual")
        self._lattice_constant = x

    @property
    def phonon_absolute_extent(self):
        """The absolute extent value. Controls how much the clouds can overlap.
        Indicates the largest possible cloud size when multi-phonon mode
        calculations are run.

        Returns
        -------
        int
        """

        if self._phonon_absolute_extent is None:
            if len(self._phonon_extent) > 0:
                return np.max(self._phonon_extent).item()
            else:
                return None
        return self._phonon_absolute_extent

    @phonon_absolute_extent.setter
    def phonon_absolute_extent(self, x):
        L = len(self._phonon_extent)
        if L > 1:
            logger.error(f"{L} > 2 unique phonons, absolute extent not set")
            return
        self._phonon_absolute_extent = x

    @property
    def n_phonon_types(self):
        """A counter which keeps track of the number of phonon types that are
        contained in the model

        Returns
        -------
        int
        """

        return self._n_phonon_types

    @n_phonon_types.setter
    def n_phonon_types(self, x):
        assert isinstance(x, int)
        self._n_phonon_types = x

    @property
    def phonon_max_per_site(self):
        """Controls the hard-boson constraint. Essentially restrains the number
        of phonons that can be on each site. If None, there is no restriction.

        Returns
        -------
        int
        """

        return self._phonon_max_per_site

    @phonon_max_per_site.setter
    def phonon_max_per_site(self, x):
        if x is not None:
            assert isinstance(x, int)
        self._phonon_max_per_site = x

    @property
    def hamiltonian(self):
        """The Hamiltonian object for this model.

        Returns
        -------
        Hamiltonian
        """

        return self._hamiltonian

    @hamiltonian.setter
    def hamiltonian(self, x):
        assert isinstance(x, Hamiltonian)
        self._hamiltonian = x

    @property
    def phonon_extent(self):
        """The list of phonon extents. Commonly referred to as ``M``.

        Returns
        -------
        list
        """

        return self._phonon_extent

    @phonon_extent.setter
    def phonon_extent(self, x):
        assert x == []
        self._phonon_extent = []

    @property
    def phonon_number(self):
        """The list of max phonons. Commonly referred to as ``N``.

        Returns
        -------
        list
        """

        return self._phonon_number

    @phonon_number.setter
    def phonon_number(self, x):
        assert x == []
        self._phonon_number = []

    def visualize(self):
        """Visualize the model you've initialized. Note, some values are
        rounded."""

        print("Hamiltonian parameters:")
        print(f"  Hopping (t)          = {self.hopping:.02e}")
        print(f"  Lattice constant (a) = {self.lattice_constant:.02e}")
        print(f"  Temperature (T)      = {self.temperature:.02e}")
        print(f"  Max bosons per site  = {self.phonon_max_per_site}")
        print(f"  Absolute extent      = {self.phonon_absolute_extent}")
        if len(self._phonon_extent) == 0:
            print("Terms not initialized...")
            return
        print("Terms:")
        d1 = self.hamiltonian.get_dict_rep()
        for ii, (phonon_index, term_list) in enumerate(d1.items()):
            M = self._phonon_extent[ii]
            N = self._phonon_number[ii]
            print(f"  Phonon type = {phonon_index} (M = {M}; N = {N})")
            for term in term_list:
                print(f"    {term}")

    @classmethod
    def from_parameters(
        cls,
        hopping=1.0,
        lattice_constant=1.0,
        temperature=0.0,
        phonon_max_per_site=None,
        dimension=1,
    ):
        """Convenience method for initializing the Model object from intuitive
        parameters. It is recommended that this classmethod is used over the
        constructor.

        Parameters
        ----------
        hopping : float
            The hopping strength :math:`t`. Default is 1.0.
        lattice_constant : float, optional
            Default is 1.0.
        temperature : float, optional
            Note that setting this > 0 will engage the Thermofield Double
            method. Default is 0.0.
        phonon_max_per_site : None, optional
            Used for hard phonon constraints. Default is None, indicating no
            limitation on the number of phonons per site.
        dimension : int, optional
            The spatial dimension of the system to consider. Default is 1.
        """

        return cls(
            lattice_constant=lattice_constant,
            temperature=temperature,
            hamiltonian=Hamiltonian(dimension=dimension, hopping=hopping),
            phonon_max_per_site=phonon_max_per_site,
            phonon_extent=[],
            phonon_number=[],
            phonon_absolute_extent=None,
            n_phonon_types=0,
        )

    def __init__(
        self,
        lattice_constant=1.0,
        temperature=0.0,
        hamiltonian=Hamiltonian(),
        phonon_max_per_site=None,
        phonon_extent=[],
        phonon_number=[],
        phonon_absolute_extent=None,
        n_phonon_types=0,
    ):
        self._lattice_constant = lattice_constant
        self._temperature = temperature
        self._hamiltonian = deepcopy(hamiltonian)
        self._phonon_max_per_site = phonon_max_per_site
        self._phonon_extent = copy(phonon_extent)
        self._phonon_number = copy(phonon_number)
        self._phonon_absolute_extent = phonon_absolute_extent
        self._n_phonon_types = n_phonon_types

    def _get_TFD_coupling_prefactors(self, Omega):
        """Gets the TFD coupling prefactors.

        .. important::

            For reference, the TFD prefactors are defined in e.g.
            [JCP 145, 224101 (2016)](https://aip.scitation.org/doi/10.1063/
            1.4971211).

        Parameters
        ----------
        Omega : float
            The (Einstein) phonon frequency.

        Returns
        -------
        tuple of float
            The modifying prefactor to the real and fictitious couplings. If
            temperature is zero, then (1, 0) is returned.
        """

        if self.temperature > 0.0:
            beta = 1.0 / self.temperature
            theta_beta = np.arctanh(np.exp(-beta * Omega / 2.0))
            V_prefactor = np.cosh(theta_beta)
            V_tilde_prefactor = np.sinh(theta_beta)
            return V_prefactor, V_tilde_prefactor
        else:
            return 1.0, 0.0

    def add_(
        self,
        coupling_type,
        phonon_frequency,
        phonon_extent,
        phonon_number,
        phonon_extent_tfd=None,
        phonon_number_tfd=None,
        coupling_strength=None,
        dimensionless_coupling_strength=None,
        phonon_index_override=None,
    ):
        """Adds an electron-phonon contribution to the model. Note that the
        user can override the boson index manually to construct more
        complicated models, such as single phonon-mode Hamiltonians but with
        multiple contributions to the coupling_strength term.

        Parameters
        ----------
        coupling_type : str
            The type of coupling to add to the Hamiltonian.
        phonon_frequency : float
            The Einstein phonon frequency corresponding to the phonon creation
            and annihilation operators. Traditionally denoted :math:`\\Omega`.
        phonon_extent : int
            Positive number for the max phonon extent for this term.
        phonon_number : int
            Positive number for the max number of phonons for this term.
        phonon_extent_tfd : int, optional
            Positive number for the max phonon extent for the TFD version of
            the term. Default is None.
        phonon_number_tfd : int, optional
            Positive number for the max number of phonons for the TFD version
            of this term. Default is None.
        coupling_strength : float, optional
            The strength of the coupling to add. This is g. Default is None.
            If None, requires `dimensionless_coupling_strength` to be set.
        dimensionless_coupling_strength : float, optional
            The dimensionless coupling strength, which is a function of the
            hopping, and phonon frequency, as well as the type of model.
            Default is None. If None, requires `coupling_strength` to be set.
        phonon_index_override : int, optional
            Overrides the internal phonon counter. Use at your own risk.
            Note that for finite-temperature simulations, these indexes should
            always come in pairs. In other words, if the override 0, then
            the TFD part of the terms will be 1. Throws an error if this number
            is odd and temperature > 0. Default is None (no override).
        """

        # Make a few aliases for easier writing
        M = phonon_extent
        N = phonon_number
        M_tfd = phonon_extent_tfd
        N_tfd = phonon_number_tfd

        if self.temperature > 0.0 and (M_tfd is None or N_tfd is None):
            logger.error("Temperature > 0 but phonon extent or number not set")
            return

        if N < 1 or M < 1:
            logger.error(
                f"Provided phonon extent={M} and number={N} must be > 1"
            )
            return

        c1 = M_tfd is not None and M_tfd < 1
        c2 = N_tfd is not None and N_tfd < 1
        if c1 or c2:
            logger.error(
                f"Provided phonon M_tfd={M} and N_tfd={N} must be > 1"
            )
            return

        c1 = coupling_strength is None
        c2 = dimensionless_coupling_strength is None
        if not (c1 ^ c2):  # XOR
            logger.error(
                "One or the other of the coupling strength or dimensionless "
                "coupling strength should be set: XOR should be True"
            )
            return

        if phonon_index_override is not None and self.temperature > 0.0:
            if phonon_index_override % 2 != 0:
                logger.error("Phonon override is odd and temperature > 0")
                return

        if self.temperature == 0 and (M_tfd is not None or N_tfd is not None):
            logger.warning(
                "Temperature is set to zero but M_tfd or N_tfd values were "
                "provided and will be ignored."
            )

        # Get the TFD prefactors for the terms in the Hamiltonian. Note that
        # if temperature = 0, V_tilde_pf will be None.
        V_pf, V_tilde_pf = self._get_TFD_coupling_prefactors(phonon_frequency)

        # Add the standard term to the Hamiltonian
        if phonon_index_override is None:
            phonon_index = self._n_phonon_types
        else:
            phonon_index = phonon_index_override
        self._hamiltonian.add_(
            coupling_type,
            phonon_index,
            phonon_frequency,
            coupling_strength,
            dimensionless_coupling_strength,
            coupling_multiplier=V_pf,
        )
        self._phonon_extent.append(phonon_extent)
        self._phonon_number.append(phonon_number)
        self._n_phonon_types += 1
        phonon_index += 1

        # Add the finite-temperature term to the Hamiltonian
        if self.temperature > 0.0:
            self._hamiltonian.add_(
                coupling_type,
                phonon_index,
                -phonon_frequency,  # Negative phonon frequency!
                coupling_strength,
                dimensionless_coupling_strength,
                coupling_multiplier=V_tilde_pf,
            )

            assert phonon_extent_tfd is not None
            assert phonon_number_tfd is not None
            self._phonon_extent.append(phonon_extent_tfd)
            self._phonon_number.append(phonon_number_tfd)
            self._n_phonon_types += 1
