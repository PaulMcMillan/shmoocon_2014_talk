from horizon import tables

class BlacklistTable(tables.DataTable):
    value = tables.Column('value')

    def get_object_id(self, datum):
        return str(datum)

    class Meta:
        name = 'blacklist'
        verbose_name = 'Blacklist'
        multi_select = False
