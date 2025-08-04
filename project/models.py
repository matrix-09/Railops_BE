from sqlalchemy import Column, String, Date, JSON
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    formNumber = Column(String, primary_key=True, index=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    formNumber = Column(String, primary_key=True, index=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    bogieDetails = Column(JSON)
    bogieChecksheet = Column(JSON)
    bmbcChecksheet = Column(JSON)
