from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Luanzim',
        email='titio.12@gmail.com',
        password='senha123',
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'titio.12@gmail.com')
    )
    assert result.username == 'Luanzim'
