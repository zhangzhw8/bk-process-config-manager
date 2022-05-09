# Generated by Django 3.2.4 on 2022-05-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gsekit", "0010_auto_20210625_1804"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="configinstance",
            options={
                "ordering": ["-id"],
                "verbose_name": "配置实例（ConfigInstance）",
                "verbose_name_plural": "配置实例（ConfigInstance）",
            },
        ),
        migrations.AlterModelOptions(
            name="configtemplate",
            options={
                "ordering": ["-config_template_id"],
                "verbose_name": "配置模板（ConfigTemplate）",
                "verbose_name_plural": "配置模板（ConfigTemplate）",
            },
        ),
        migrations.AlterModelOptions(
            name="configtemplatebindingrelationship",
            options={
                "verbose_name": "配置模板与进程的绑定关系（ConfigTemplateBindingRelationship）",
                "verbose_name_plural": "配置模板与进程的绑定关系（ConfigTemplateBindingRelationship）",
            },
        ),
        migrations.AlterModelOptions(
            name="configtemplateversion",
            options={
                "ordering": ["-config_version_id"],
                "verbose_name": "配置模板版本（ConfigTemplateVersion）",
                "verbose_name_plural": "配置模板版本（ConfigTemplateVersion）",
            },
        ),
        migrations.AlterModelOptions(
            name="globalsettings",
            options={"verbose_name": "全局配置表（GlobalSettings）", "verbose_name_plural": "全局配置表（GlobalSettings）"},
        ),
        migrations.AlterModelOptions(
            name="job",
            options={"ordering": ("-id",), "verbose_name": "任务（Job）", "verbose_name_plural": "任务历史（Job）"},
        ),
        migrations.AlterModelOptions(
            name="jobtask",
            options={"verbose_name": "任务详情（JobTask）", "verbose_name_plural": "任务详情（JobTask）"},
        ),
        migrations.AlterModelOptions(
            name="process",
            options={"verbose_name": "业务进程（Process）", "verbose_name_plural": "业务进程（Process）"},
        ),
        migrations.AlterModelOptions(
            name="processinst",
            options={"verbose_name": "进程实例（ProcessInst）", "verbose_name_plural": "进程实例（ProcessInst）"},
        ),
        migrations.AddField(
            model_name="job",
            name="task_granularity",
            field=models.CharField(db_index=True, default="BIZ", max_length=32, verbose_name="任务聚合粒度"),
        ),
    ]