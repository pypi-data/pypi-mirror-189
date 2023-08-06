from dataclasses import dataclass
from typing import List, Optional

import algosdk
import algosdk.transaction


@dataclass
class AlgoUser:
    """A simple Algorand user storing an address and private key.

    Parameters
    ----------
    address
        The base32 Algorand address of the user.
    private_key
        The private key of the user.
    name
        A name assigned to the user for better pretty-printing.
    """

    address: str
    """Stored user address from the constructor."""

    private_key: Optional[str] = None
    """Stored user private key from the constructor."""

    name: Optional[str] = None
    """Stored user name from the constructor."""

    def __str__(self) -> str:
        str_identifier = self.name if self.name else self.address
        return f"AlgoUser({repr(str_identifier)})"

    def __repr__(self) -> str:
        return f"AlgoUser(address={repr(self.address)}, private_key={repr(self.private_key)}, name={repr(self.name)})"


_NullUser = AlgoUser(address="")


class SmartContractAccount(AlgoUser):
    """An Algorand user subclass representing a smart contract's account address.

    Parameters
    ----------
    app_id
        The ID of the application for this account address.
    name
        A name assigned to the application account for better pretty-printing.
    """

    def __init__(self, app_id: int, name: Optional[str] = None):
        self._app_id = app_id

        smart_contract_address = algosdk.logic.get_application_address(app_id)

        # Instantiate the super `AlgoUser` class
        super().__init__(address=smart_contract_address, name=name)

    def __str__(self) -> str:
        str_identifier = self.name if self.name else self.address
        return f"SmartContractAccount({repr(str_identifier)})"

    def __repr__(self) -> str:
        return (
            f"SmartContractAccount(app_id={repr(self._app_id)}, name={repr(self.name)})"
        )


class MultisigAccount(AlgoUser):
    """An Algorand user subclass representing a multi-signature account.

    Parameters
    ----------
    version
        The version of the multi-signature account.
    threshold
        The minimum number of owner signers required to operate the multi-signature account.
    owner_accounts
        The owners of the multi-signature account.
    name
        A name assigned to the multi-signature account for better pretty-printing.
    """

    def __init__(
        self,
        version: int,
        threshold: int,
        owner_accounts: List[AlgoUser],
        name: Optional[str] = None,
    ):
        # Save the passed in values privately
        self._version = version
        self._threshold = threshold
        self._owner_accounts = owner_accounts

        # Instantiate the super `AlgoUser` class
        super().__init__(address=self.attributes.address(), name=name)

    @property
    def attributes(self) -> algosdk.transaction.Multisig:
        """The multi-signature attributes enforced on this multi-signature account."""
        # Return a fresh `Multisig` object every time `self.attributes` is called.
        # This is because if the attributes are used to sign a `MultisigTransaction`,
        # they may no longer be reused to sign a different `MultisigTransaction`
        owners_pub_keys = [owner.address for owner in self._owner_accounts]
        return algosdk.transaction.Multisig(
            self._version, self._threshold, owners_pub_keys
        )

    def __str__(self) -> str:
        if self.name:
            str_identifier = f"'{self.name}'"
        else:
            str_identifier = ", ".join([str(owner) for owner in self._owner_accounts])
        return f"MultisigAccount({str_identifier})"

    def __repr__(self) -> str:
        return f"MultisigAccount(version={repr(self._version)}, threshold={repr(self._threshold)}, owner_accounts={repr(self._owner_accounts)}, name={repr(self.name)})"
