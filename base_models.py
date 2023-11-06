from pydantic import BaseModel


class SignatureFieldTimestamps(BaseModel):
    checkbox: str
    initial: str
    signature: str


class Timestamps(BaseModel):
    createdOn: str
    openedOn: str
    signatureFields: SignatureFieldTimestamps
    completedAt: str


class FinalizedServiceAgreement(BaseModel):
    agreement: str
    customer: str
    signature: str
    timestamps: Timestamps
