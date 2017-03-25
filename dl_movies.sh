#!/bin/bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/movie/popular?page=' + page + '&language=en-US&api_key=15e1fa139021ce8ffbda7a3ca062f2fc' \
  --data '{}'
