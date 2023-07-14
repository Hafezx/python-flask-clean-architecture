import redis
import config

r = redis.Redis(
    host=config.REDIS_HOST,
    password=config.REDIS_PASS,
    port=config.REDIS_PORT)


def is_redis_available():
    # ... get redis connection here, or pass it in. up to you.
    try:
        r.get(None)  # getting None returns None or throws an exception
    except (redis.exceptions.ConnectionError,
            redis.exceptions.BusyLoadingError):
        print("err 2  redis")
        return False
    return True


def redis_instance():
    return r


def set_otp_for_user_in_redis(_key, _maps):
    pattern = 'otp_' + _key
    try:
        print(int(config.REDIS_EXP_TIME))
        r.set(pattern, str(_maps), int(config.REDIS_EXP_TIME))
        # r.hset(name=pattern, mapping=_maps, expiration_time=10)
    except Exception as e:
        #  log
        print(e)
        print("failed to connect to redis")
        pass


def check_if_otp_send_for_user_or_not(_key):
    pattern = 'otp_' + _key
    try:
        resp = r.get(pattern)
        if resp is None:
            return False
        else:
            return True
    except Exception as e:
        #  log
        print(e)
        print("failed to connect to redis")
        return False


def get_data_by_mobile_if_in_redis(_key):
    pattern = 'otp_' + _key
    try:
        resp = r.get(pattern)
        return resp
    except Exception as e:
        #  log
        print(e)
        print("failed to connect to redis")
        return None


def delete_otp_from_redis(_key):
    pattern = 'otp_' + _key
    try:
        r.delete(pattern)
        return True
    except Exception as e:
        #  log
        print(e)
        print("failed to connect to redis")
        return False
