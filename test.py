import sys
import datetime
import os
import pdb

def test_logger():
    """Test logger.

    :return: logger or False
    :rtype: logging.Logger or bool
    """
    from src import mylogger
    try:
        m = mylogger.get_logger('test', '/home/ubuntu/Data_Architecture/log')
        m.debug('hi, debug')
    except Exception as e:
        print(e)
        return False
    return m

def test_config():
    """Test config.

    :return: test result
    :rtype: bool
    """
    from src import myconfig
    try:
        project_root_path = os.getenv("DA_DESIGN_SERVER")
        m = myconfig.get_config('{}/share/test.config'.format(project_root_path))
        print('key1=', m['general'].get('key1'))
        print('key2=', m['general'].get('key2'))
        print('key3=', m['logger'].get('key3'))
    except Exception as e:
        print(e)
        return False
    return True

def test_login(logger):
    """Test login process.

    :param logger: logger instance
    :type logger: logging.Logger
    :return: test result
    :rtype: bool
    """
    from src import user
    session_key = user.login('iam', 'biggong', logger)
    if not session_key:
        return False

    what_time_is_it = datetime.datetime.now()
    doc_user_result = user.check_session( \
            session_key["session_id"],
            what_time_is_it.timestamp())
    if not doc_user_result:
        return False
    print("session user = {}".format(doc_user_result["user_id"]))
    return True

if __name__ == '__main__':
    target_step = []
    if len(sys.argv) >= 2:
        target_step = sys.argv[1].split(',')
    print('Test steps = ', target_step)

    logger = test_logger()
    if not logger:
        raise Exception('Error when test_logger')
    print('Success - test_logger')

    if not target_step or 'config' in target_step:
        ret = test_config()
        if not ret:
            raise Exception('Error when test_config')
        print('Success - test_config')

    if not target_step or 'login' in target_step:
        ret = test_login(logger)
        if not ret:
            raise Exception('Error when test_login')
        print('Success - test_login')

    print('Test completed.')

