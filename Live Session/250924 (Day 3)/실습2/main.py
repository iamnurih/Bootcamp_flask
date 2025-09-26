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

def run_bulk():
    db = SessionLocal()

    # new_users = ([User(name="Han_River"), User(name="Han_리버"), User(name="Han_한리버"), User(name="Han_리버바보"), User(name="Han_River")])
    # db.add_all(new_users)
    # db.commit()

    users = db.query(User).all()
    for user in users:
        print(user)

    #조건부 조회
    # real_user = db.query(User).filter(User.name == "Han_River").first()
    # print("진짜 한리버찾기", real_user)
    #
    han_users = db.query(User).filter(User.name.like("Han_%")).all()
    for han_user in han_users:
        print("Han 포함된 이름 찾기", han_user)
    #
    # for u in users:
    #     u.name = u.name + "_NEW"

    han_users = db.query(User).filter(User.name.like("%_바보_%")).all()
    for han_user in han_users:
        db.delete(han_user)


    db.commit()

    users = db.query(User).all()
    for user in users:
     print("한 삭제 완료", user)

    db.commit()

    db.close()


if __name__ == '__main__':
    run_bulk()

