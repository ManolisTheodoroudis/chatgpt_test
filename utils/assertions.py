from config.config import CONF


class Assert():

    @staticmethod
    def are_equal(expected, actual, message ):
        CONF.logger.info(f"assert are_equal {expected} : {actual}, {message}")
        assert expected == actual , message

    @staticmethod
    def is_true(condition, message ):
        CONF.logger.info(f"assert is true {condition} , {message}")
        assert condition == True, message

    @staticmethod
    def contains(expected, actual, message ):
        CONF.logger.info(f"assert contains {expected} : {actual}, {message}")
        assert expected in actual , message
