from pathlib import Path
from typing import Optional, Dict, Any, List, Union
from typing_extensions import Literal

from phidata.app.airflow.airflow_base import (
    AirflowBase,
    AirflowLogsVolumeType,
    ServiceType,
    DbApp,
    WorkspaceVolumeType,
    ImagePullPolicy,
)


class AirflowManager(AirflowBase):
    def __init__(
        self,
        name: str = "airflow-manager",
        version: str = "1",
        enabled: bool = True,
        # -*- Image Configuration,
        # Image can be provided as a DockerImage object or as image_name:image_tag
        image: Optional[Any] = None,
        image_name: str = "phidata/airflow",
        image_tag: str = "2.5.0",
        entrypoint: Optional[Union[str, List]] = "/scripts/manager",
        command: Optional[Union[str, List]] = None,
        # Install python dependencies using a requirements.txt file,
        install_requirements: bool = False,
        # Path to the requirements.txt file relative to the workspace_root,
        requirements_file: str = "requirements.txt",
        # -*- Airflow Configuration,
        # The AIRFLOW_ENV defines the current airflow runtime and can be used by,
        # DAGs to separate dev/stg/prd code,
        airflow_env: Optional[str] = None,
        # Set the AIRFLOW_HOME env variable,
        # Defaults to container env variable: /usr/local/airflow,
        airflow_home: Optional[str] = None,
        # If use_products_as_airflow_dags = True,
        # set the AIRFLOW__CORE__DAGS_FOLDER to the products_dir,
        use_products_as_airflow_dags: bool = True,
        # If use_products_as_airflow_dags = False,
        # set the AIRFLOW__CORE__DAGS_FOLDER to the airflow_dags_path,
        # airflow_dags_path is the directory in the container containing the airflow dags,
        airflow_dags_path: Optional[str] = None,
        # Creates an airflow admin with username: admin, pass: admin,
        create_airflow_admin_user: bool = False,
        # Airflow Executor,
        executor: str = "SequentialExecutor",
        # Configure airflow db,
        # If init_airflow_db = True, initialize the airflow_db,
        init_airflow_db: bool = False,
        # Upgrade the airflow db,
        upgrade_airflow_db: bool = False,
        wait_for_db: bool = False,
        # delay start by 60 seconds for the db to be initialized,
        wait_for_db_init: bool = False,
        # Connect to database using a DbApp,
        db_app: Optional[DbApp] = None,
        # Provide database connection details manually,
        # db_user can be provided here or as the,
        # DATABASE_USER env var in the secrets_file,
        db_user: Optional[str] = None,
        # db_password can be provided here or as the,
        # DATABASE_PASSWORD env var in the secrets_file,
        db_password: Optional[str] = None,
        # db_schema can be provided here or as the,
        # DATABASE_DB env var in the secrets_file,
        db_schema: Optional[str] = None,
        # db_host can be provided here or as the,
        # DATABASE_HOST env var in the secrets_file,
        db_host: Optional[str] = None,
        # db_port can be provided here or as the,
        # DATABASE_PORT env var in the secrets_file,
        db_port: Optional[int] = None,
        # db_driver can be provided here or as the,
        # DATABASE_DRIVER env var in the secrets_file,
        db_driver: str = "postgresql+psycopg2",
        db_result_backend_driver: str = "db+postgresql",
        # Airflow db connections in the format { conn_id: conn_url },
        # converted to env var: AIRFLOW_CONN__conn_id = conn_url,
        db_connections: Optional[Dict] = None,
        # Configure airflow redis,
        wait_for_redis: bool = False,
        # Connect to redis using a PhidataApp,
        redis_app: Optional[DbApp] = None,
        # Provide redis connection details manually,
        # redis_password can be provided here or as the,
        # REDIS_PASSWORD env var in the secrets_file,
        redis_password: Optional[str] = None,
        # redis_schema can be provided here or as the,
        # REDIS_SCHEMA env var in the secrets_file,
        redis_schema: Optional[str] = None,
        # redis_host can be provided here or as the,
        # REDIS_HOST env var in the secrets_file,
        redis_host: Optional[str] = None,
        # redis_port can be provided here or as the,
        # REDIS_PORT env var in the secrets_file,
        redis_port: Optional[int] = None,
        # redis_driver can be provided here or as the,
        # REDIS_DRIVER env var in the secrets_file,
        redis_driver: Optional[str] = None,
        # -*- Container Configuration,
        container_name: Optional[str] = None,
        # Overwrite the PYTHONPATH env var,,
        # which is usually set to the workspace_root_container_path,
        python_path: Optional[str] = None,
        # Add to the PYTHONPATH env var. If python_path is set, this is ignored
        # Does not overwrite the PYTHONPATH env var - adds to it.
        add_python_path: Optional[str] = None,
        # Add labels to the container,
        container_labels: Optional[Dict[str, Any]] = None,
        # Container env passed to the PhidataApp,
        # Add env variables to container env,
        env: Optional[Dict[str, str]] = None,
        # Read env variables from a file in yaml format,
        env_file: Optional[Path] = None,
        # Container secrets,
        # Add secret variables to container env,
        secrets: Optional[Dict[str, str]] = None,
        # Read secret variables from a file in yaml format,
        secrets_file: Optional[Path] = None,
        # Read secret variables from AWS Secrets,
        aws_secrets: Optional[Any] = None,
        # Container ports,
        # Open a container port if open_container_port=True,
        open_container_port: bool = False,
        # Port number on the container,
        container_port: int = 8000,
        # Port name: Only used by the K8sContainer,
        container_port_name: str = "http",
        # Host port: Only used by the DockerContainer,
        container_host_port: int = 8000,
        # Open the webserver port if open_webserver_port=True,
        open_webserver_port: bool = False,
        # Webserver port number on the container,
        webserver_port: int = 8080,
        # Port name: Only used by the K8sContainer,
        webserver_port_name: str = "webserver",
        # Host port: Only used by the DockerContainer,
        webserver_host_port: int = 8080,
        # Open the worker_log_port if open_worker_log_port=True,
        # When you start an airflow worker, airflow starts a tiny web server subprocess to serve the workers,
        # local log files to the airflow main web server, which then builds pages and sends them to users.,
        # This defines the port on which the logs are served. It needs to be unused, and open visible from,
        # the main web server to connect into the workers.,
        open_worker_log_port: bool = False,
        worker_log_port: int = 8793,
        # Port name: Only used by the K8sContainer,
        worker_log_port_name: str = "worker",
        # Host port: Only used by the DockerContainer,
        worker_log_host_port: int = 8793,
        # Open the flower port if open_flower_port=True,
        open_flower_port: bool = False,
        # Flower port number on the container,
        flower_port: int = 5555,
        # Port name: Only used by the K8sContainer,
        flower_port_name: str = "flower",
        # Host port: Only used by the DockerContainer,
        flower_host_port: int = 5555,
        # Container volumes,
        # Mount the workspace directory on the container,
        mount_workspace: bool = False,
        workspace_volume_name: Optional[str] = None,
        workspace_volume_type: Optional[WorkspaceVolumeType] = None,
        # Path to mount the workspace volume,
        # This is the parent directory for the workspace on the container,
        # i.e. the ws is mounted as a subdir in this dir,
        # eg: if ws name is: idata, workspace_root would be: /mnt/workspaces/idata,
        workspace_volume_container_path: str = "/mnt/workspaces",
        # How to mount the workspace volume,
        # Option 1: Mount the workspace from the host machine,
        # If None, use the workspace_root_path,
        # Note: This is the default on DockerContainers. We assume that DockerContainers,
        # are running locally on the user's machine so the local workspace_root_path,
        # is mounted to the workspace_volume_container_path,
        workspace_volume_host_path: Optional[str] = None,
        # Option 2: Load the workspace from git using a git-sync sidecar container,
        # This the default on K8sContainers.,
        create_git_sync_sidecar: bool = False,
        # Required to create an initial copy of the workspace,
        create_git_sync_init_container: bool = True,
        git_sync_image_name: str = "k8s.gcr.io/git-sync",
        git_sync_image_tag: str = "v3.1.1",
        git_sync_repo: Optional[str] = None,
        git_sync_branch: Optional[str] = None,
        git_sync_wait: int = 1,
        # Mount the logs directory on the container,
        mount_logs: bool = True,
        logs_volume_name: Optional[str] = None,
        logs_volume_type: AirflowLogsVolumeType = AirflowLogsVolumeType.EmptyDir,
        # Container path to mount the volume,
        # - If logs_volume_container_path is provided, use that,
        # - If logs_volume_container_path is None and airflow_home is set,
        #       use airflow_home/logs,
        # - If logs_volume_container_path is None and airflow_home is None,
        #       use "/usr/local/airflow/logs",
        logs_volume_container_path: Optional[str] = None,
        # Logs PersistentVolume configuration,
        logs_pv_labels: Optional[Dict[str, str]] = None,
        # AccessModes is a list of ways the volume can be mounted.,
        # More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes,
        # Type: phidata.infra.k8s.enums.pv.PVAccessMode
        logs_pv_access_modes: Optional[List[Any]] = None,
        logs_pv_requests_storage: Optional[str] = None,
        # A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.,
        # More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options,
        logs_pv_mount_options: Optional[List[str]] = None,
        # What happens to a persistent volume when released from its claim.,
        #   The default policy is Retain.,
        logs_pv_reclaim_policy: Optional[Literal["Delete", "Recycle", "Retain"]] = None,
        logs_pv_storage_class: str = "",
        # Logs EFS configuration,
        # EFS volume_id,
        logs_efs_volume_id: Optional[str] = None,
        # -*- Docker configuration,
        # Run container in the background and return a Container object.,
        container_detach: bool = True,
        # Enable auto-removal of the container on daemon side when the container’s process exits.,
        container_auto_remove: bool = True,
        # Remove the container when it has finished running. Default: True.,
        container_remove: bool = True,
        # Username or UID to run commands as inside the container.,
        container_user: Optional[Union[str, int]] = None,
        # Keep STDIN open even if not attached.,
        container_stdin_open: bool = True,
        container_tty: bool = True,
        # Specify a test to perform to check that the container is healthy.,
        container_healthcheck: Optional[Dict[str, Any]] = None,
        # Optional hostname for the container.,
        container_hostname: Optional[str] = None,
        # Platform in the format os[/arch[/variant]].,
        container_platform: Optional[str] = None,
        # Path to the working directory.,
        container_working_dir: Optional[str] = None,
        # Restart the container when it exits. Configured as a dictionary with keys:,
        # Name: One of on-failure, or always.,
        # MaximumRetryCount: Number of times to restart the container on failure.,
        # For example: {"Name": "on-failure", "MaximumRetryCount": 5},
        container_restart_policy_docker: Optional[Dict[str, Any]] = None,
        # Add volumes to DockerContainer,
        # container_volumes is a dictionary which adds the volumes to mount,
        # inside the container. The key is either the host path or a volume name,,
        # and the value is a dictionary with 2 keys:,
        #   bind - The path to mount the volume inside the container,
        #   mode - Either rw to mount the volume read/write, or ro to mount it read-only.,
        # For example:,
        # {,
        #   '/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},,
        #   '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'},
        # },
        container_volumes_docker: Optional[Dict[str, dict]] = None,
        # Add ports to DockerContainer,
        # The keys of the dictionary are the ports to bind inside the container,,
        # either as an integer or a string in the form port/protocol, where the protocol is either tcp, udp.,
        # The values of the dictionary are the corresponding ports to open on the host, which can be either:,
        #   - The port number, as an integer.,
        #       For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.,
        #   - None, to assign a random host port. For example, {'2222/tcp': None}.,
        #   - A tuple of (address, port) if you want to specify the host interface.,
        #       For example, {'1111/tcp': ('127.0.0.1', 1111)}.,
        #   - A list of integers, if you want to bind multiple host ports to a single container port.,
        #       For example, {'1111/tcp': [1234, 4567]}.,
        container_ports_docker: Optional[Dict[str, Any]] = None,
        # -*- K8s configuration,
        # K8s Deployment configuration,
        replicas: int = 1,
        pod_name: Optional[str] = None,
        deploy_name: Optional[str] = None,
        secret_name: Optional[str] = None,
        configmap_name: Optional[str] = None,
        # Type: ImagePullPolicy,
        image_pull_policy: Optional[ImagePullPolicy] = None,
        pod_annotations: Optional[Dict[str, str]] = None,
        pod_node_selector: Optional[Dict[str, str]] = None,
        # Type: RestartPolicy,
        deploy_restart_policy: Optional[Any] = None,
        deploy_labels: Optional[Dict[str, Any]] = None,
        termination_grace_period_seconds: Optional[int] = None,
        # How to spread the deployment across a topology,
        # Key to spread the pods across,
        topology_spread_key: Optional[str] = None,
        # The degree to which pods may be unevenly distributed,
        topology_spread_max_skew: Optional[int] = None,
        # How to deal with a pod if it doesn't satisfy the spread constraint.,
        topology_spread_when_unsatisfiable: Optional[str] = None,
        # K8s Service Configuration,
        create_service: bool = False,
        service_name: Optional[str] = None,
        # Type: ServiceType,
        service_type: Optional[Any] = None,
        # The port exposed by the service.,
        service_port: int = 8000,
        # The node_port exposed by the service if service_type = ServiceType.NODE_PORT,
        service_node_port: Optional[int] = None,
        # The target_port is the port to access on the pods targeted by the service.,
        # It can be the port number or port name on the pod.,
        service_target_port: Optional[Union[str, int]] = None,
        # Extra ports exposed by the webserver service. Type: List[CreatePort],
        service_ports: Optional[List[Any]] = None,
        # Service labels,
        service_labels: Optional[Dict[str, Any]] = None,
        # Service annotations,
        service_annotations: Optional[Dict[str, str]] = None,
        # If ServiceType == ServiceType.LoadBalancer,
        service_health_check_node_port: Optional[int] = None,
        service_internal_traffic_policy: Optional[str] = None,
        service_load_balancer_class: Optional[str] = None,
        service_load_balancer_ip: Optional[str] = None,
        service_load_balancer_source_ranges: Optional[List[str]] = None,
        service_allocate_load_balancer_node_ports: Optional[bool] = None,
        create_webserver_service: bool = False,
        # Configure the webserver service,
        ws_svc_name: Optional[str] = None,
        ws_svc_type: Optional[ServiceType] = None,
        # The port exposed by the webserver service.,
        ws_svc_port: int = 8080,
        # The node_port exposed by the service if ws_svc_type = ServiceType.NODE_PORT,
        ws_node_port: Optional[int] = None,
        # The ws_target_port is the port to access on the pods targeted by the service.,
        # It can be the port number or port name on the pod.,
        ws_target_port: Optional[Union[str, int]] = None,
        # Extra ports exposed by the webserver service,
        ws_svc_ports: Optional[List[Any]] = None,
        # Add labels to webserver service,
        ws_svc_labels: Optional[Dict[str, Any]] = None,
        # Add annotations to webserver service,
        ws_svc_annotations: Optional[Dict[str, str]] = None,
        # If ServiceType == LoadBalancer,
        ws_svc_health_check_node_port: Optional[int] = None,
        ws_svc_internal_taffic_policy: Optional[str] = None,
        ws_svc_load_balancer_class: Optional[str] = None,
        ws_svc_load_balancer_ip: Optional[str] = None,
        ws_svc_load_balancer_source_ranges: Optional[List[str]] = None,
        ws_svc_allocate_load_balancer_node_ports: Optional[bool] = None,
        # Configure the flower service,
        create_flower_service: bool = False,
        flower_svc_name: Optional[str] = None,
        flower_svc_type: Optional[ServiceType] = None,
        # The port exposed by the service.,
        flower_svc_port: int = 5555,
        # The node_port exposed by the service if ws_svc_type = ServiceType.NODE_PORT,
        flower_node_port: Optional[int] = None,
        # The flower_target_port is the port to access on the pods targeted by the service.,
        # It can be the port number or port name on the pod.,
        flower_target_port: Optional[Union[str, int]] = None,
        # Extra ports exposed by the flower service,
        flower_svc_ports: Optional[List[Any]] = None,
        # Add labels to flower service,
        flower_svc_labels: Optional[Dict[str, Any]] = None,
        # Add annotations to flower service,
        flower_svc_annotations: Optional[Dict[str, str]] = None,
        # If ServiceType == LoadBalancer,
        flower_svc_health_check_node_port: Optional[int] = None,
        flower_svc_internal_taffic_policy: Optional[str] = None,
        flower_svc_load_balancer_class: Optional[str] = None,
        flower_svc_load_balancer_ip: Optional[str] = None,
        flower_svc_load_balancer_source_ranges: Optional[List[str]] = None,
        flower_svc_allocate_load_balancer_node_ports: Optional[bool] = None,
        # K8s RBAC Configuration,
        use_rbac: bool = False,
        # Create a Namespace with name ns_name & default values,
        ns_name: Optional[str] = None,
        # or Provide the full Namespace definition,
        # Type: CreateNamespace,
        namespace: Optional[Any] = None,
        # Create a ServiceAccount with name sa_name & default values,
        sa_name: Optional[str] = None,
        # or Provide the full ServiceAccount definition,
        # Type: CreateServiceAccount,
        service_account: Optional[Any] = None,
        # Create a ClusterRole with name cr_name & default values,
        cr_name: Optional[str] = None,
        # or Provide the full ClusterRole definition,
        # Type: CreateClusterRole,
        cluster_role: Optional[Any] = None,
        # Create a ClusterRoleBinding with name crb_name & default values,
        crb_name: Optional[str] = None,
        # or Provide the full ClusterRoleBinding definition,
        # Type: CreateClusterRoleBinding,
        cluster_role_binding: Optional[Any] = None,
        # Add additional Kubernetes resources to the App,
        # Type: CreateSecret,
        extra_secrets: Optional[List[Any]] = None,
        # Type: CreateConfigMap,
        extra_configmaps: Optional[List[Any]] = None,
        # Type: CreateService,
        extra_services: Optional[List[Any]] = None,
        # Type: CreateDeployment,
        extra_deployments: Optional[List[Any]] = None,
        # Type: CreatePersistentVolume,
        extra_pvs: Optional[List[Any]] = None,
        # Type: CreatePVC,
        extra_pvcs: Optional[List[Any]] = None,
        # Type: CreateContainer,
        extra_containers: Optional[List[Any]] = None,
        # Type: CreateContainer,
        extra_init_containers: Optional[List[Any]] = None,
        # Type: CreatePort,
        extra_ports: Optional[List[Any]] = None,
        # Type: CreateVolume,
        extra_volumes: Optional[List[Any]] = None,
        # Type: CreateStorageClass,
        extra_storage_classes: Optional[List[Any]] = None,
        # Type: CreateCustomObject,
        extra_custom_objects: Optional[List[Any]] = None,
        # Type: CreateCustomResourceDefinition,
        extra_crds: Optional[List[Any]] = None,
        # Other args,
        load_examples: bool = False,
        print_env_on_load: bool = True,
        # If True, skip resource creation if active resources with the same name exist.,
        use_cache: bool = True,
        **kwargs,
    ):
        super().__init__(
            name=name,
            version=version,
            enabled=enabled,
            image=image,
            image_name=image_name,
            image_tag=image_tag,
            entrypoint=entrypoint,
            command=command,
            install_requirements=install_requirements,
            requirements_file=requirements_file,
            airflow_env=airflow_env,
            airflow_home=airflow_home,
            use_products_as_airflow_dags=use_products_as_airflow_dags,
            airflow_dags_path=airflow_dags_path,
            create_airflow_admin_user=create_airflow_admin_user,
            executor=executor,
            init_airflow_db=init_airflow_db,
            upgrade_airflow_db=upgrade_airflow_db,
            wait_for_db=wait_for_db,
            wait_for_db_init=wait_for_db_init,
            db_app=db_app,
            db_user=db_user,
            db_password=db_password,
            db_schema=db_schema,
            db_host=db_host,
            db_port=db_port,
            db_driver=db_driver,
            db_result_backend_driver=db_result_backend_driver,
            db_connections=db_connections,
            wait_for_redis=wait_for_redis,
            redis_app=redis_app,
            redis_password=redis_password,
            redis_schema=redis_schema,
            redis_host=redis_host,
            redis_port=redis_port,
            redis_driver=redis_driver,
            container_name=container_name,
            python_path=python_path,
            add_python_path=add_python_path,
            container_labels=container_labels,
            env=env,
            env_file=env_file,
            secrets=secrets,
            secrets_file=secrets_file,
            aws_secrets=aws_secrets,
            open_container_port=open_container_port,
            container_port=container_port,
            container_port_name=container_port_name,
            container_host_port=container_host_port,
            open_webserver_port=open_webserver_port,
            webserver_port=webserver_port,
            webserver_port_name=webserver_port_name,
            webserver_host_port=webserver_host_port,
            open_worker_log_port=open_worker_log_port,
            worker_log_port=worker_log_port,
            worker_log_port_name=worker_log_port_name,
            worker_log_host_port=worker_log_host_port,
            open_flower_port=open_flower_port,
            flower_port=flower_port,
            flower_port_name=flower_port_name,
            flower_host_port=flower_host_port,
            mount_workspace=mount_workspace,
            workspace_volume_name=workspace_volume_name,
            workspace_volume_type=workspace_volume_type,
            workspace_volume_container_path=workspace_volume_container_path,
            workspace_volume_host_path=workspace_volume_host_path,
            create_git_sync_sidecar=create_git_sync_sidecar,
            create_git_sync_init_container=create_git_sync_init_container,
            git_sync_image_name=git_sync_image_name,
            git_sync_image_tag=git_sync_image_tag,
            git_sync_repo=git_sync_repo,
            git_sync_branch=git_sync_branch,
            git_sync_wait=git_sync_wait,
            mount_logs=mount_logs,
            logs_volume_name=logs_volume_name,
            logs_volume_type=logs_volume_type,
            logs_volume_container_path=logs_volume_container_path,
            logs_pv_labels=logs_pv_labels,
            logs_pv_access_modes=logs_pv_access_modes,
            logs_pv_requests_storage=logs_pv_requests_storage,
            logs_pv_mount_options=logs_pv_mount_options,
            logs_pv_reclaim_policy=logs_pv_reclaim_policy,
            logs_pv_storage_class=logs_pv_storage_class,
            logs_efs_volume_id=logs_efs_volume_id,
            container_detach=container_detach,
            container_auto_remove=container_auto_remove,
            container_remove=container_remove,
            container_user=container_user,
            container_stdin_open=container_stdin_open,
            container_tty=container_tty,
            container_healthcheck=container_healthcheck,
            container_hostname=container_hostname,
            container_platform=container_platform,
            container_working_dir=container_working_dir,
            container_restart_policy_docker=container_restart_policy_docker,
            container_volumes_docker=container_volumes_docker,
            container_ports_docker=container_ports_docker,
            replicas=replicas,
            pod_name=pod_name,
            deploy_name=deploy_name,
            secret_name=secret_name,
            configmap_name=configmap_name,
            image_pull_policy=image_pull_policy,
            pod_annotations=pod_annotations,
            pod_node_selector=pod_node_selector,
            deploy_restart_policy=deploy_restart_policy,
            deploy_labels=deploy_labels,
            termination_grace_period_seconds=termination_grace_period_seconds,
            topology_spread_key=topology_spread_key,
            topology_spread_max_skew=topology_spread_max_skew,
            topology_spread_when_unsatisfiable=topology_spread_when_unsatisfiable,
            create_service=create_service,
            service_name=service_name,
            service_type=service_type,
            service_port=service_port,
            service_node_port=service_node_port,
            service_target_port=service_target_port,
            service_ports=service_ports,
            service_labels=service_labels,
            service_annotations=service_annotations,
            service_health_check_node_port=service_health_check_node_port,
            service_internal_traffic_policy=service_internal_traffic_policy,
            service_load_balancer_class=service_load_balancer_class,
            service_load_balancer_ip=service_load_balancer_ip,
            service_load_balancer_source_ranges=service_load_balancer_source_ranges,
            service_allocate_load_balancer_node_ports=service_allocate_load_balancer_node_ports,
            create_webserver_service=create_webserver_service,
            ws_svc_name=ws_svc_name,
            ws_svc_type=ws_svc_type,
            ws_svc_port=ws_svc_port,
            ws_node_port=ws_node_port,
            ws_target_port=ws_target_port,
            ws_svc_ports=ws_svc_ports,
            ws_svc_labels=ws_svc_labels,
            ws_svc_annotations=ws_svc_annotations,
            ws_svc_health_check_node_port=ws_svc_health_check_node_port,
            ws_svc_internal_taffic_policy=ws_svc_internal_taffic_policy,
            ws_svc_load_balancer_class=ws_svc_load_balancer_class,
            ws_svc_load_balancer_ip=ws_svc_load_balancer_ip,
            ws_svc_load_balancer_source_ranges=ws_svc_load_balancer_source_ranges,
            ws_svc_allocate_load_balancer_node_ports=ws_svc_allocate_load_balancer_node_ports,
            create_flower_service=create_flower_service,
            flower_svc_name=flower_svc_name,
            flower_svc_type=flower_svc_type,
            flower_svc_port=flower_svc_port,
            flower_node_port=flower_node_port,
            flower_target_port=flower_target_port,
            flower_svc_ports=flower_svc_ports,
            flower_svc_labels=flower_svc_labels,
            flower_svc_annotations=flower_svc_annotations,
            flower_svc_health_check_node_port=flower_svc_health_check_node_port,
            flower_svc_internal_taffic_policy=flower_svc_internal_taffic_policy,
            flower_svc_load_balancer_class=flower_svc_load_balancer_class,
            flower_svc_load_balancer_ip=flower_svc_load_balancer_ip,
            flower_svc_load_balancer_source_ranges=flower_svc_load_balancer_source_ranges,
            flower_svc_allocate_load_balancer_node_ports=flower_svc_allocate_load_balancer_node_ports,
            use_rbac=use_rbac,
            ns_name=ns_name,
            namespace=namespace,
            sa_name=sa_name,
            service_account=service_account,
            cr_name=cr_name,
            cluster_role=cluster_role,
            crb_name=crb_name,
            cluster_role_binding=cluster_role_binding,
            extra_secrets=extra_secrets,
            extra_configmaps=extra_configmaps,
            extra_services=extra_services,
            extra_deployments=extra_deployments,
            extra_pvs=extra_pvs,
            extra_pvcs=extra_pvcs,
            extra_containers=extra_containers,
            extra_init_containers=extra_init_containers,
            extra_ports=extra_ports,
            extra_volumes=extra_volumes,
            extra_storage_classes=extra_storage_classes,
            extra_custom_objects=extra_custom_objects,
            extra_crds=extra_crds,
            load_examples=load_examples,
            print_env_on_load=print_env_on_load,
            use_cache=use_cache,
            **kwargs,
        )
