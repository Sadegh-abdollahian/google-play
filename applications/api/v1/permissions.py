# from rest_framework.permissions import BasePermission


# class IsDeveloperOrReadonly(BasePermission):

#     def has_permission(self, request, view):
#         ip_addr = request.META["REMOTE_ADDR"]
#         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked
