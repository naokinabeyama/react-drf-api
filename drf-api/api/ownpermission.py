from rest_framework import permissions



class ProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS 新規作成、取得だけ
        # リクエストされたメソッドが新規作成、取得に当てはまった場合Trueを返す
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
