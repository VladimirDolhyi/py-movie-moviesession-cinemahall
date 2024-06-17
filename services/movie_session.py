from django.db.models import QuerySet

import datetime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime.datetime,
        movie_id: str,
        cinema_hall_id: str) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime.datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie=movie_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
