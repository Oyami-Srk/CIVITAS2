# Generated by Django 3.2.5 on 2021-08-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkillModel', '0025_skillname_userbigskill_usersmallskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbigskill',
            name='caifa',
            field=models.FloatField(default=0, verbose_name='采伐技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='caifa_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='采伐等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='gengzuo',
            field=models.FloatField(default=0, verbose_name='耕作技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='gengzuo_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='耕作等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='jiagong',
            field=models.FloatField(default=0, verbose_name='加工技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='jiagong_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='加工等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='jianshe',
            field=models.FloatField(default=0, verbose_name='建设技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='jianshe_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='建设等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='shejiao',
            field=models.FloatField(default=0, verbose_name='社交技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='shejiao_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='社交等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='xumu',
            field=models.FloatField(default=0, verbose_name='畜牧技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='xumu_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='畜牧等级'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='zhouche',
            field=models.FloatField(default=0, verbose_name='舟车技能点'),
        ),
        migrations.AlterField(
            model_name='userbigskill',
            name='zhouche_level',
            field=models.SmallIntegerField(choices=[(1, '学徒'), (2, '匠人'), (3, '匠师'), (4, '专家'), (5, '大师'), (6, '宗师'), (7, '大宗师')], default=1, verbose_name='舟车等级'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='bulao',
            field=models.FloatField(default=0, verbose_name='舟车——捕捞技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='caiji',
            field=models.FloatField(default=0, verbose_name='采伐——采集技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='famu',
            field=models.FloatField(default=0, verbose_name='采伐——伐木技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='fangzhi',
            field=models.FloatField(default=0, verbose_name='加工——纺织技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='guanli',
            field=models.FloatField(default=0, verbose_name='社交——管理技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jiachu',
            field=models.FloatField(default=0, verbose_name='畜牧——家畜养殖技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jianzhu',
            field=models.FloatField(default=0, verbose_name='建设——建筑技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jiaoji',
            field=models.FloatField(default=0, verbose_name='社交——交际技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jiaqin',
            field=models.FloatField(default=0, verbose_name='畜牧——家禽养殖技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jingji',
            field=models.FloatField(default=0, verbose_name='耕作——经济作物种植技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='jinsu',
            field=models.FloatField(default=0, verbose_name='加工——金属锻造技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='kaicai',
            field=models.FloatField(default=0, verbose_name='采伐——开采技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='kaiken',
            field=models.FloatField(default=0, verbose_name='耕作——开垦技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='kantan',
            field=models.FloatField(default=0, verbose_name='采伐——勘探技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='liangshi',
            field=models.FloatField(default=0, verbose_name='耕作——粮食种植技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='lushang',
            field=models.FloatField(default=0, verbose_name='舟车——陆上运输技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='mushi',
            field=models.FloatField(default=0, verbose_name='加工——木石加工技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='shiping',
            field=models.FloatField(default=0, verbose_name='加工——食品加工技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='shoulie',
            field=models.FloatField(default=0, verbose_name='畜牧——狩猎技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='shuishang',
            field=models.FloatField(default=0, verbose_name='舟车——水上运输技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='suguo',
            field=models.FloatField(default=0, verbose_name='耕作——蔬果种植技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='wenshu',
            field=models.FloatField(default=0, verbose_name='社交——文书技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='xiongbian',
            field=models.FloatField(default=0, verbose_name='社交——雄辩技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='xiushan',
            field=models.FloatField(default=0, verbose_name='建设——修缮技能点'),
        ),
        migrations.AlterField(
            model_name='usersmallskill',
            name='yelian',
            field=models.FloatField(default=0, verbose_name='加工——冶炼技能点'),
        ),
    ]
