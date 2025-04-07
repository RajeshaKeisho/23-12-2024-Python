from django.core.paginator import Paginator, Page

class LimitOffsetPage(Page):
    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_previous(self):
        return self.number > 1

    def next_page_number(self):
        return self.paginator.num_pages

    def previous_page_number(self):
        return 1

class LimitOffsetPaginator(Paginator):
    def __init__(self, object_list, limit=None, offset=0):
        self.limit = int(limit) if limit is not None else len(object_list)
        self.offset = int(offset)
        super().__init__(object_list, self.limit)

    def _get_page(self, *args, **kwargs):
        return LimitOffsetPage(*args, **kwargs)

    def page(self, number):
        bottom = self.offset
        top = bottom + self.per_page
        return self._get_page(self.object_list[bottom:top], number, self)

class CursorPaginator(Paginator):
    def __init__(self, object_list, cursor=None, per_page=10):
        self.cursor = cursor
        self.per_page = per_page
        super().__init__(object_list, self.per_page)

    def _get_page(self, *args, **kwargs):
        return Page(*args, **kwargs)

    def page(self, number):
        if self.cursor:
            index = self.object_list.index(self.cursor) if self.cursor in self.object_list else 0
        else:
            index = 0
        bottom = index
        top = bottom + self.per_page
        return self._get_page(self.object_list[bottom:top], number, self)
