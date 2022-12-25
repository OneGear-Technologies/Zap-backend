# Zap-backend
Backend repo for zap scan and pay infra

## Register User
Api endpoint for user registraiton is at `api/register` attributes are 
> Username(Phone Number)*, Password**, Email Address, Firstname, Lastname

## Login endpoint

The endpoint for login is `/api/login/` and endpoint for login refresh is at `/api/login/refresh`.

This will return
* refresh token('refresh')
* access token('access')