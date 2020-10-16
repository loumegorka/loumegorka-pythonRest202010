"""
schema.py : model to be converted in json by fastapi
"""
from typing import Optional, List
from datetime import date

from pydantic import BaseModel


class StarBase(BaseModel):

    name: str
    birthdate: Optional[date]


class StarCreate(StarBase):

    pass


class Star(StarBase):

    id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):

    title: str
    year: int
    duration: Optional[int]


class MovieCreate(MovieBase):

    pass


class Movie(MovieBase):

    id: int

    class Config:
        orm_mode = True


class MovieDetail(Movie):

    director: Optional[Star] = None
    actors: List[Star] = []

class MovieStat(BaseModel):

    year: int
    movie_count: int
    min_duration: Optional[int]
    max_duration: Optional[int]
    avg_duration: Optional[float]

class DirectorStat(BaseModel):

    director: Star
    movie_count: int

class StarBirthyearStat(BaseModel):

    birthyear: int
    star_count: int

class StarStat(BaseModel):
    
    actor: Star
    movie_count : int
    first_movie_year: int
    last_movie_year: int