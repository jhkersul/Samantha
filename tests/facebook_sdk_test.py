import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAPY18XApoME1AbQGZAZAaQpAWWhfD1BWsZAwECUFW5E8611mNI62YGOUWkVCuWtZAutW2bUxvQlfyxOSVisvjEC9ATaK6Sa6uokxOC6Th8mma8Rg1T3MJ0cdgZBhZBNopJylT5elS7jzYxZC8idwxvc7yoGK2LaLbWbtXIZBmSsS9okRa9489cgVI2yjaGfhhwZDZD', version='2.7')

graph.put_object(parent_object='me', connection_name='feed',
                 message='Samantha disse oi!')
