# Ros2

This is a basic implementation of 2 Ros2 nodes communicating
over the same network. One node publishes while the other subscribes.

The bash scripts run both of the nodes and sets and environment variable
for the nodes to communicate through, essentially the nodeA publishes to
the variabe name as a topic name. NodeB grabs the info from the topic.

Do not run the nodes individually this will not work, just run the scripts.

Launch script run_node_a.sh first, lauch run_node_b.sh next.