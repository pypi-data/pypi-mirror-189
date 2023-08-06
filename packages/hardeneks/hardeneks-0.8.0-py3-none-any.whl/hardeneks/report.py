from rich.table import Table
from rich.panel import Panel

from hardeneks import console


def print_role_table(roles, message, docs, type):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for role in roles:
        table.add_row(type, role.metadata.namespace, role.metadata.name)

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_instance_metadata_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("HttpPutResponseHopLimit", style="magenta")

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(
                instance["Instances"][0]["MetadataOptions"][
                    "HttpPutResponseHopLimit"
                ]
            ),
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_instance_public_table(instances, message, docs):
    table = Table()

    table.add_column("InstanceId", style="cyan")
    table.add_column("PublicDnsName", style="magenta")

    for instance in instances:
        table.add_row(
            instance["Instances"][0]["InstanceId"],
            str(instance["Instances"][0]["PublicDnsName"]),
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_node_table(nodes, message, docs):
    table = Table()

    table.add_column("NodeName", style="cyan")

    for node in nodes:
        table.add_row(node.metadata.name)
    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_repository_table(repositories, attribute, message, docs):
    table = Table()
    table.add_column("Repository", style="cyan")
    table.add_column(attribute, style="magenta")
    for repository in repositories:
        table.add_row(
            repository["repositoryName"],
            repository[attribute],
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_pod_table(pods, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for pod in pods:
        table.add_row("Pod", pod.metadata.namespace, pod.metadata.name)

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_workload_table(workloads, message, docs, kind):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in workloads:
        table.add_row(
            kind, workload.metadata.namespace, workload.metadata.name
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_namespace_table(namespaces, message, docs):
    table = Table()

    table.add_column("Namespace", style="cyan")

    for namespace in namespaces:
        table.add_row(
            namespace,
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_service_table(services, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in services:
        table.add_row(
            "Service", workload.metadata.namespace, workload.metadata.name
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_deployment_table(deployments, message, docs):
    table = Table()

    table.add_column("Kind", style="cyan")
    table.add_column("Namespace", style="magenta")
    table.add_column("Name", style="green")

    for workload in deployments:
        table.add_row(
            "Deployment", workload.metadata.namespace, workload.metadata.name
        )

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_storage_class_table(storage_classes, message, docs):
    table = Table()

    table.add_column("StorageClass", style="cyan")
    table.add_column("Encyrpted", style="magenta")

    for storage_class in storage_classes:
        table.add_row(storage_class.metadata.name, "false")

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_persistent_volume_table(persistent_volumes, message, docs):
    table = Table()

    table.add_column("PersistentVolume", style="cyan")
    table.add_column("Encrypted", style="magenta")

    for persistent_volume in persistent_volumes:
        table.add_row(persistent_volume.metadata.name, "false")

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()


def print_role_action_table(actions, message, docs):
    table = Table()
    table.add_column("Action", style="cyan")

    for action in actions:
        table.add_row(action)

    console.print(Panel(table, title=message, subtitle=docs))
    console.print()
