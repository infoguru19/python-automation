import shutil
import datetime

source = "/etc"
backup_name = f"/tmp/etc_backup_{datetime.date.today()}"

shutil.make_archive(backup_name, "zip", source)
print("Backup completed successfully")
