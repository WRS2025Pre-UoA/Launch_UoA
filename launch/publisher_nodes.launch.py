from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # launchの構成を示すLaunchDescription型の変数の定義
    ld = LaunchDescription()

    # publisher node "Pressure"
    pub_node1 = Node(
        package='pressure',
        executable='pressure_subscriber',
        name='pressure',
        remappings=[('image_topic', 'pressure_image')]
    )

    # publisher node "QR"
    pub_node2 = Node(
        package='scan_qr',
        executable='listener',
        name='qr',
        remappings=[('image_raw', 'qr_image'), ('qr_image', 'qr_result_image'),
                    ("qr_value", "qr_result_value")]
    )

    # publisher node "QR_M"
    pub_node3 = Node(
        package='manual_package',
        executable='manual_publisher',
        name='qr_manual',
        remappings=[('manual_input_qr', 'qr_image_manual'),('text_topic','qr_result_value')]
    )

    # publisher node "Crack"
    pub_node4 = Node(
        package='crack',
        executable='crack_subscriber',
        name='crack',
        remappings=[('image_raw', 'crack_image')]
    )

    pub_node5 = Node(
        package='tree_publisher',
        executable='tree_publisher',
        name='tree',
        remappings=[
            ('input_image_topic', '/arm_camera/image_raw/decompressed')]
    )

    pub_node6 = Node(
        package='digital_twin_client',
        executable='digital_twin_client',
        name='dt_client',
        remappings=[('send_image', 'send_topic')],
        parameters=[{"host": "", "robot_id": ""}]  # サーバの値を設定する
    )

    pub_node7 = Node(
        package='photo',
        executable='photo_sub_pub',
        name='photo',
        remappings=[('input_photo_image','situation_image')]
    )

    pub_node8 = Node(
        package='bulb',
        executable='bulb_param',
        name='bulb',
        remappings=[('input_bulb_image','bulb_image')]
    )

    # LaunchDescriptionに、起動したいノードを追加する
    ld.add_action(pub_node1)
    ld.add_action(pub_node2)
    ld.add_action(pub_node3)
    ld.add_action(pub_node4)
    ld.add_action(pub_node5)
    ld.add_action(pub_node6)
    ld.add_action(pub_node7)
    ld.add_action(pub_node8)

    # launch構成を返すようにする
    return ld
