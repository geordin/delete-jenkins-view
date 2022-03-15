import jenkins

server = jenkins.Jenkins('URL', username='USER', password='PASS')

views = server.get_views()
view_names = [li['name'] for li in views]

view_exclude = ['VIEW1', 'VIEW2']

for item in view_names:
    if item not in view_exclude:
        server.delete_view(item)
views = server.get_views()
print (views)
