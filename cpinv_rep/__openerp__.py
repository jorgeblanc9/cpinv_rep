# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
#   jorgescalona@riseup.net   @jorgemustaine  https://github.com/jorgescalona
#
##############################################################################
{
    "name" : "cpinv_rep",
    "version" : "0.1.0",
    "website" : "http://www.attakatara.wordpress.com",
    "description" : "agrega la posibilidad de generar reportes a cpsis, se debe instalar la \
                    libreria wkhtmltopdf en su version 0.12.0 para el funcionamiento correcto \
                    del motor de informes",
    "author" : "jorgescalona @jorgemustaine",
    "depends" : ['cpinv_base','report_webkit'],
    "data" : ['views/template_reporte_cpinv.xml','reportes/reportes_cpinv.xml'],
    "installable": True,
}
