from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name = {self.name})>"

engine = create_engine('sqlite:///:users.db', echo=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)

def run_single():
    db = SessionLocal()

    new_user = User(name="River")
    db.add(new_user)
    db.commit()

    # users = db.query(User).all()
    user = db.query(User).first() #단일 유저 조회
    print("유저 조회 완료", user)

    #update
    user.name = "리버바보"
    db.commit()

    user = db.query(User).first() #단일 유저 조회
    print("유저 수정 조회 완료", user)

    db.delete(user)
    db.commit() #데이터 저장

    user = db.query(User).all()
    print("유저 삭제 확인", user)

    db.close()


if __name__ == '__main__':
    run_single()

