# Generated by Django 4.2.4 on 2023-11-02 12:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_answer_excludedcontrols_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='excludedControls',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Control 1'), (2, 'Control 2'), (3, 'Control 3'), (4, 'Control 4'), (5, 'Control 5'), (6, 'Control 6'), (7, 'Control 7'), (8, 'Control 8'), (9, 'Control 9'), (10, 'Control 10'), (11, 'Control 11'), (12, 'Control 12'), (13, 'Control 13'), (14, 'Control 14'), (15, 'Control 15'), (16, 'Control 16'), (17, 'Control 17'), (18, 'Control 18'), (19, 'Control 19'), (20, 'Control 20'), (21, 'Control 21'), (22, 'Control 22'), (23, 'Control 23'), (24, 'Control 24'), (25, 'Control 25'), (26, 'Control 26'), (27, 'Control 27'), (28, 'Control 28'), (29, 'Control 29'), (30, 'Control 30'), (31, 'Control 31'), (32, 'Control 32'), (33, 'Control 33'), (34, 'Control 34'), (35, 'Control 35'), (36, 'Control 36'), (37, 'Control 37'), (38, 'Control 38'), (39, 'Control 39'), (40, 'Control 40'), (41, 'Control 41'), (42, 'Control 42'), (43, 'Control 43'), (44, 'Control 44'), (45, 'Control 45'), (46, 'Control 46'), (47, 'Control 47'), (48, 'Control 48'), (49, 'Control 49'), (50, 'Control 50'), (51, 'Control 51'), (52, 'Control 52'), (53, 'Control 53'), (54, 'Control 54'), (55, 'Control 55'), (56, 'Control 56'), (57, 'Control 57'), (58, 'Control 58'), (59, 'Control 59'), (60, 'Control 60'), (61, 'Control 61'), (62, 'Control 62'), (63, 'Control 63'), (64, 'Control 64'), (65, 'Control 65'), (66, 'Control 66'), (67, 'Control 67'), (68, 'Control 68'), (69, 'Control 69'), (70, 'Control 70'), (71, 'Control 71'), (72, 'Control 72'), (73, 'Control 73'), (74, 'Control 74'), (75, 'Control 75'), (76, 'Control 76'), (77, 'Control 77'), (78, 'Control 78'), (79, 'Control 79'), (80, 'Control 80'), (81, 'Control 81'), (82, 'Control 82'), (83, 'Control 83'), (84, 'Control 84'), (85, 'Control 85'), (86, 'Control 86'), (87, 'Control 87'), (88, 'Control 88'), (89, 'Control 89'), (90, 'Control 90'), (91, 'Control 91'), (92, 'Control 92'), (93, 'Control 93'), (94, 'Control 94'), (95, 'Control 95'), (96, 'Control 96'), (97, 'Control 97'), (98, 'Control 98'), (99, 'Control 99'), (100, 'Control 100'), (101, 'Control 101'), (102, 'Control 102'), (103, 'Control 103'), (104, 'Control 104'), (105, 'Control 105'), (106, 'Control 106'), (107, 'Control 107'), (108, 'Control 108'), (109, 'Control 109'), (110, 'Control 110'), (111, 'Control 111'), (112, 'Control 112'), (113, 'Control 113'), (114, 'Control 114'), (115, 'Control 115'), (116, 'Control 116'), (117, 'Control 117'), (118, 'Control 118'), (119, 'Control 119'), (120, 'Control 120'), (121, 'Control 121'), (122, 'Control 122'), (123, 'Control 123'), (124, 'Control 124'), (125, 'Control 125'), (126, 'Control 126'), (127, 'Control 127'), (128, 'Control 128'), (129, 'Control 129'), (130, 'Control 130'), (131, 'Control 131'), (132, 'Control 132'), (133, 'Control 133'), (134, 'Control 134'), (135, 'Control 135'), (136, 'Control 136'), (137, 'Control 137'), (138, 'Control 138'), (139, 'Control 139'), (140, 'Control 140'), (141, 'Control 141'), (142, 'Control 142'), (143, 'Control 143'), (144, 'Control 144'), (145, 'Control 145'), (146, 'Control 146'), (147, 'Control 147'), (148, 'Control 148'), (149, 'Control 149'), (150, 'Control 150'), (151, 'Control 151'), (152, 'Control 152'), (153, 'Control 153'), (154, 'Control 154'), (155, 'Control 155'), (156, 'Control 156'), (157, 'Control 157'), (158, 'Control 158'), (159, 'Control 159'), (160, 'Control 160'), (161, 'Control 161'), (162, 'Control 162'), (163, 'Control 163'), (164, 'Control 164'), (165, 'Control 165'), (166, 'Control 166'), (167, 'Control 167'), (168, 'Control 168'), (169, 'Control 169'), (170, 'Control 170'), (171, 'Control 171'), (172, 'Control 172'), (173, 'Control 173'), (174, 'Control 174'), (175, 'Control 175'), (176, 'Control 176'), (177, 'Control 177'), (178, 'Control 178'), (179, 'Control 179'), (180, 'Control 180'), (181, 'Control 181'), (182, 'Control 182'), (183, 'Control 183'), (184, 'Control 184'), (185, 'Control 185'), (186, 'Control 186'), (187, 'Control 187'), (188, 'Control 188'), (189, 'Control 189'), (190, 'Control 190'), (191, 'Control 191'), (192, 'Control 192'), (193, 'Control 193'), (194, 'Control 194'), (195, 'Control 195'), (196, 'Control 196'), (197, 'Control 197'), (198, 'Control 198'), (199, 'Control 199'), (200, 'Control 200'), (201, 'Control 201'), (202, 'Control 202'), (203, 'Control 203'), (204, 'Control 204'), (205, 'Control 205'), (206, 'Control 206'), (207, 'Control 207'), (208, 'Control 208'), (209, 'Control 209'), (210, 'Control 210'), (211, 'Control 211'), (212, 'Control 212'), (213, 'Control 213'), (214, 'Control 214'), (215, 'Control 215'), (216, 'Control 216'), (217, 'Control 217'), (218, 'Control 218'), (219, 'Control 219'), (220, 'Control 220'), (221, 'Control 221'), (222, 'Control 222'), (223, 'Control 223'), (224, 'Control 224'), (225, 'Control 225'), (226, 'Control 226'), (227, 'Control 227'), (228, 'Control 228'), (229, 'Control 229'), (230, 'Control 230'), (231, 'Control 231'), (232, 'Control 232'), (233, 'Control 233'), (234, 'Control 234'), (235, 'Control 235'), (236, 'Control 236'), (237, 'Control 237'), (238, 'Control 238'), (239, 'Control 239'), (240, 'Control 240'), (241, 'Control 241'), (242, 'Control 242'), (243, 'Control 243'), (244, 'Control 244'), (245, 'Control 245'), (246, 'Control 246'), (247, 'Control 247'), (248, 'Control 248'), (249, 'Control 249'), (250, 'Control 250'), (251, 'Control 251'), (252, 'Control 252'), (253, 'Control 253'), (254, 'Control 254'), (255, 'Control 255'), (256, 'Control 256'), (257, 'Control 257'), (258, 'Control 258'), (259, 'Control 259'), (260, 'Control 260'), (261, 'Control 261'), (262, 'Control 262'), (263, 'Control 263'), (264, 'Control 264'), (265, 'Control 265'), (266, 'Control 266'), (267, 'Control 267'), (268, 'Control 268'), (269, 'Control 269'), (270, 'Control 270'), (271, 'Control 271'), (272, 'Control 272'), (273, 'Control 273'), (274, 'Control 274'), (275, 'Control 275'), (276, 'Control 276'), (277, 'Control 277'), (278, 'Control 278'), (279, 'Control 279'), (280, 'Control 280'), (281, 'Control 281'), (282, 'Control 282'), (283, 'Control 283'), (284, 'Control 284'), (285, 'Control 285'), (286, 'Control 286'), (287, 'Control 287'), (288, 'Control 288'), (289, 'Control 289'), (290, 'Control 290'), (291, 'Control 291'), (292, 'Control 292'), (293, 'Control 293'), (294, 'Control 294'), (295, 'Control 295'), (296, 'Control 296'), (297, 'Control 297'), (298, 'Control 298'), (299, 'Control 299'), (300, 'Control 300'), (301, 'Control 301'), (302, 'Control 302'), (303, 'Control 303'), (304, 'Control 304'), (305, 'Control 305'), (306, 'Control 306'), (307, 'Control 307'), (308, 'Control 308'), (309, 'Control 309'), (310, 'Control 310'), (311, 'Control 311'), (312, 'Control 312'), (313, 'Control 313'), (314, 'Control 314'), (315, 'Control 315'), (316, 'Control 316'), (317, 'Control 317'), (318, 'Control 318'), (319, 'Control 319'), (320, 'Control 320'), (321, 'Control 321'), (322, 'Control 322'), (323, 'Control 323'), (324, 'Control 324'), (325, 'Control 325'), (326, 'Control 326'), (327, 'Control 327'), (328, 'Control 328'), (329, 'Control 329'), (330, 'Control 330'), (331, 'Control 331'), (332, 'Control 332'), (333, 'Control 333'), (334, 'Control 334'), (335, 'Control 335'), (336, 'Control 336'), (337, 'Control 337'), (338, 'Control 338'), (339, 'Control 339'), (340, 'Control 340'), (341, 'Control 341'), (342, 'Control 342'), (343, 'Control 343'), (344, 'Control 344'), (345, 'Control 345'), (346, 'Control 346'), (347, 'Control 347'), (348, 'Control 348'), (349, 'Control 349'), (350, 'Control 350'), (351, 'Control 351'), (352, 'Control 352'), (353, 'Control 353'), (354, 'Control 354'), (355, 'Control 355'), (356, 'Control 356'), (357, 'Control 357'), (358, 'Control 358'), (359, 'Control 359'), (360, 'Control 360'), (361, 'Control 361'), (362, 'Control 362'), (363, 'Control 363'), (364, 'Control 364'), (365, 'Control 365'), (366, 'Control 366'), (367, 'Control 367'), (368, 'Control 368'), (369, 'Control 369'), (370, 'Control 370'), (371, 'Control 371'), (372, 'Control 372'), (373, 'Control 373'), (374, 'Control 374'), (375, 'Control 375'), (376, 'Control 376'), (377, 'Control 377'), (378, 'Control 378'), (379, 'Control 379'), (380, 'Control 380'), (381, 'Control 381'), (382, 'Control 382'), (383, 'Control 383'), (384, 'Control 384'), (385, 'Control 385'), (386, 'Control 386'), (387, 'Control 387'), (388, 'Control 388'), (389, 'Control 389'), (390, 'Control 390'), (391, 'Control 391'), (392, 'Control 392'), (393, 'Control 393'), (394, 'Control 394'), (395, 'Control 395'), (396, 'Control 396'), (397, 'Control 397'), (398, 'Control 398'), (399, 'Control 399'), (400, 'Control 400'), (401, 'Control 401'), (402, 'Control 402'), (403, 'Control 403'), (404, 'Control 404'), (405, 'Control 405'), (406, 'Control 406'), (407, 'Control 407'), (408, 'Control 408')], max_length=100, null=True, verbose_name='Controles excluidos'),
        ),
    ]
