from database.models import User
from database.models import async_session
from sqlalchemy import select

class UserRegistration:
    def __init__(self, usr_id, username):
        self.usr_id = usr_id
        self.username = username

    async def req_registration(self):
        async with async_session() as session:
            result = await session.execute(select(User).where((User.usr_id == self.usr_id) & (User.username == self.username)))
            identity = result.scalar_one_or_none()
            if not identity:
                session.add(User(usr_id=self.usr_id, username=self.username))
                await session.commit()


