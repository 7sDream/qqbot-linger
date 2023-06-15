import nonebot
from nonebot.adapters.onebot.v11 import Adapter


def main():
    nonebot.init(_env_file=".env")

    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    nonebot.load_builtin_plugins()
    nonebot.load_plugin("nonebot_plugin_apscheduler")
    nonebot.load_plugin("nonebot_plugin_bam")
    nonebot.load_plugin("nonebot_plugin_7s_roll")

    nonebot.run()


if __name__ == "__main__":
    main()
