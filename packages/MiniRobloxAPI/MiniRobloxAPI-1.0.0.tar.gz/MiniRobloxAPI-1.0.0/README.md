# MiniRobloxAPI
![PyPI Python Version](https://img.shields.io/pypi/pyversions/fortnite-api?label=python%20version&logo=python&logoColor=yellow)

Easy to use MiniRobloxAPI module.


## Installing

Python 3.5 or higher is required

```
pip install MiniRobloxAPI
```

## Documentation

To get started we first need to import the api and initialize the client.

```
import MiniRobloxAPI

api = MiniRobloxAPI.RobloxAPI
```

## Get user
```
api.get_user_by_id(user_id)
api.get_user_by_name(user_name)
```
# Attributes:
name, user_id, description, created, is_banned, has_verified_badge, display_name, avatar_image

## Get group
```
api.get_group_by_id(group_id)
```
# Attributes:
name, group_id, description, icon_image, created, has_verified_badge, owner

## Get Badge
```
api.get_badge_by_id(badge_id)
```
# Attributes:
name, badge_id, description, created, updated, past_day_awarded_count, awarded_count, rarity, icon_image