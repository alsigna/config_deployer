from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_scrapli.tasks import send_command, send_config
from nornir_utils.plugins.functions import print_result


def deploy_interface(task):
    # generate config from template file for each device
    config = task.run(
        task=template_file,
        name="generate config",
        template="interface.j2",
        path="./templates",
    )
    task.host["config"] = config.result

    # sending config to the box and write mem
    task.run(
        task=send_config,
        name="send config",
        dry_run=False,
        config=task.host["config"],
    )

    task.run(
        task=send_command,
        name="save config",
        command="write memory",
    )


if __name__ == "__main__":
    nr = InitNornir(config_file="./config.yml")
    job = nr.run(task=deploy_interface)
    print_result(job)
