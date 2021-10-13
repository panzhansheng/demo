from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from config import engine

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Account(Base):
    __tablename__ = 'course_account'
    account = Column(String(255), primary_key=True)
    psw = Column(String(255))
    email = Column(String(255))
    isActive = Column(String(255))
    isAdmin = Column(String(255))

    def __repr__(self):
        return "<Account(account='%s', psw='%s', email='%s'), isActive='%s', isAdmin='%s'>" % (
                                self.account, self.psw, self.email, self.isActive, self.isAdmin)

class FileInfo(Base):
    __tablename__ = 'course_fileinfo'
    fileID = Column(Integer, Sequence('fileID'), primary_key=True)
    fileName = Column(String(255))
    filePath = Column(String(255))
    fileUpDate = Column(String(255))
    fileTypeID = Column(Integer)
    stulevelID = Column(Integer)

    def __repr__(self):
        return "<FileInfo(fileID='%s', fileName='%s', filePath='%s'), fileUpDate='%s', fileTypeID='%s', stulevelID='%s'>" % (
                                self.fileID, self.fileName, self.filePath, self.fileUpDate, self.fileTypeID, self.stulevelID)


acc = Account(account='pzf', psw='1qaz@WSX', email='20200331006@163.com',isActive='1', isAdmin='0')
#session.add(acc)
print(f'acc={acc.account}')
file = session.query(FileInfo).filter_by(fileName='实例分割示例').first()
print(f'filePath={file.filePath}')
session.commit()
