import pandas as pd

class ExcelGenerator:
    def __init__(self, list, filename):
        self.list = list
        self.filename = filename

    # Generates and writes data resulted from scrape to Excel file on corresponding module directory
    def generate(self):
        df = pd.DataFrame([x.values() for x in self.list],
                          columns=self.list[0].keys())
        writer = pd.ExcelWriter(
            self.filename,
            engine="xlsxwriter",
            engine_kwargs={
                "options": {"strings_to_numbers": True, "strings_to_urls": False}
            },
        )
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        workbook = writer.book
        header_fmt = workbook.add_format(
            {
                "bold": 1,
                "border": 1,
                "align": "left",
                "valign": "vcenter",
            }
        )
        writer.sheets["Sheet1"].freeze_panes(1, 0)
        for col_num, value in enumerate(df.columns.values):
            writer.sheets["Sheet1"].write(0, col_num, value, header_fmt)
            writer.sheets["Sheet1"].set_column("A:Z", 22)
        writer.save()


