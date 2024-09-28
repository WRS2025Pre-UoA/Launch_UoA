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
        #namespace='pressure',                 # namespace_app2というnamespaceを追加
        remappings=[('image_topic', 'pressure_image')]    # chatterトピックをchatter_app2トピックにremap
    )

    # publisher node "QR"
    pub_node2 = Node(
        package='scan_qr',
        executable='listener',
        name='listener',
        #namespace='pressure',                 # namespace_app2というnamespaceを追加
        remappings=[('image_raw', 'qr_image'),('qr_image','qr_result_image'),("qr_value","qr_result_value")]    # chatterトピックをchatter_app2トピックにremap
    )

    # publisher node "Rust"
    pub_node3 = Node(
        package='rust',
        executable='rust_subscriber',
        name='rust',
        #namespace='rust',                 # namespace_app1というnamespaceを追加
        remappings=[('image_topic', 'rust_image')]    # chatterトピックをchatter_app1トピックにremap
    )

    # publisher node "Crack"
    pub_node4 = Node(
        package='crack',
        executable='crack_subscriber',
        name='crack',
        #namespace='crack',                 # namespace_app1というnamespaceを追加
        remappings=[('image_raw', 'crack_image')]    # chatterトピックをchatter_app1トピックにremap
    )

    pub_node5 = Node(
        package='tree_publisher',
        executable='tree_publisher',
        # name='tree',
        #namespace='crack',                 # namespace_app1というnamespaceを追加
        remappings=[('input_image_topic', '/arm_camera/image_raw/decompressed')]    # chatterトピックをchatter_app1トピックにremap
    )

    pub_node6 = Node(
        package='digital_twin_client',
        executable='digital_twin_client',
        # name='tree',
        #namespace='crack',                 # namespace_app1というnamespaceを追加
        remappings=[('send_image', 'send_topic')]    # chatterトピックをchatter_app1トピックにremap
    )

    # pub_node6 = Node(
    #     package='temp_publisher',
    #     executable='temp_publisher',
    #     name='temp'
    #     #namespace='crack',                 # namespace_app1というnamespaceを追加
    #     # remappings=[('image_raw', 'crack_image')]    # chatterトピックをchatter_app1トピックにremap
    # )



    # publisher nodeを、"talker_renamed1"という名前で定義
    # pub_node6 = Node(
    #     package='send',
    #     executable='image_subscriber',
    #     name='crack_subscriber',
    #     #namespace='crack',                 # namespace_app1というnamespaceを追加
    #     remappings=[('image_raw', 'crack_image')]    # chatterトピックをchatter_app1トピックにremap
    # )


    # LaunchDescriptionに、起動したいノードを追加する
    ld.add_action(pub_node1)
    ld.add_action(pub_node2)
    ld.add_action(pub_node3)
    ld.add_action(pub_node4)
    ld.add_action(pub_node5)
    ld.add_action(pub_node6)

    # launch構成を返すようにする
    return ld
