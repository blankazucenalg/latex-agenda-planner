import subprocess
from calendar import monthrange
from datetime import date
from enum import Enum
from string import Template


class LaTexDelimiterTemplate(Template):
    delimiter = '__'


class FontFamily(Enum):
    SANS_SERIF = 'sfdefault'
    SERIF = 'rmdefault'
    MONOSPACE = 'ttdefault'

    def __str__(self):
        return str(self.value)


class LaTexColor(Enum):
    Apricot = 'Apricot'
    Aquamarine = 'Aquamarine'
    Bittersweet = 'Bittersweet'
    Black = 'Black'
    Blue = 'Blue'
    BlueGreen = 'BlueGreen'
    BlueViolet = 'BlueViolet'
    BrickRed = 'BrickRed'
    Brown = 'Brown'
    BurntOrange = 'BurntOrange'
    CadetBlue = 'CadetBlue'
    CarnationPink = 'CarnationPink'
    Cerulean = 'Cerulean'
    CornflowerBlue = 'CornflowerBlue'
    Cyan = 'Cyan'
    Dandelion = 'Dandelion'
    DarkOrchid = 'DarkOrchid'
    Emerald = 'Emerald'
    ForestGreen = 'ForestGreen'
    Fuchsia = 'Fuchsia'
    Goldenrod = 'Goldenrod'
    Gray = 'Gray'
    Green = 'Green'
    GreenYellow = 'GreenYellow'
    JungleGreen = 'JungleGreen'
    Lavender = 'Lavender'
    LimeGreen = 'LimeGreen'
    Magenta = 'Magenta'
    Mahogany = 'Mahogany'
    Maroon = 'Maroon'
    Melon = 'Melon'
    MidnightBlue = 'MidnightBlue'
    Mulberry = 'Mulberry'
    NavyBlue = 'NavyBlue'
    OliveGreen = 'OliveGreen'
    Orange = 'Orange'
    OrangeRed = 'OrangeRed'
    Orchid = 'Orchid'
    Peach = 'Peach'
    Periwinkle = 'Periwinkle'
    PineGreen = 'PineGreen'
    Plum = 'Plum'
    ProcessBlue = 'ProcessBlue'
    Purple = 'Purple'
    RawSienna = 'RawSienna'
    Red = 'Red'
    RedOrange = 'RedOrange'
    RedViolet = 'RedViolet'
    Rhodamine = 'Rhodamine'
    RoyalBlue = 'RoyalBlue'
    RoyalPurple = 'RoyalPurple'
    RubineRed = 'RubineRed'
    Salmon = 'Salmon'
    SeaGreen = 'SeaGreen'
    Sepia = 'Sepia'
    SkyBlue = 'SkyBlue'
    SpringGreen = 'SpringGreen'
    Tan = 'Tan'
    TealBlue = 'TealBlue'
    Thistle = 'Thistle'
    Turquoise = 'Turquoise'
    Violet = 'Violet'
    VioletRed = 'VioletRed'
    White = 'White'
    WildStrawberry = 'WildStrawberry'
    Yellow = 'Yellow'
    YellowGreen = 'YellowGreen'
    YellowOrange = 'YellowOrange'

    def __str__(self):
        return str(self.value)


class PlannerLanguages(Enum):
    ES = {
        'personal_data': 'Datos personales',
        'name': 'Nombre',
        'phone': 'Tel\\\'efono',
        'cellphone': 'Celular',
        'email': 'E-mail',
        'birthday': 'Cumplea\\~nos',
        'blood_type': 'Tipo de sangre',
        'zip_code': 'C.P.',
        'address': 'Direcci\\\'on',
        'allergies': 'Alergias',
        'in_case_emergency': 'En caso de emergencia informar a',
        'notes': 'Notas',
        'months': {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
                   8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'},
        'weekday': {0: 'Lunes', 1: 'Martes', 2: 'Mi\\\'ercoles', 3: 'Jueves', 4: 'Viernes', 5: 'S\\\'abado',
                    6: 'Domingo'}
    }
    EN = {
        'personal_data': 'Personal information',
        'name': 'Name',
        'phone': 'Phone',
        'cellphone': 'Cellphone',
        'email': 'E-mail',
        'birthday': 'Birthday',
        'blood_type': 'Blood type',
        'zip_code': 'ZIP Code',
        'address': 'Address',
        'allergies': 'Allergies',
        'in_case_emergency': 'In case of emergency inform',
        'notes': 'Notes',
        'months': {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                   8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'},
        'weekday': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday',
                    6: 'Sunday'}
    }

    def __str__(self):
        return str(self.value)


class LaTexPlanner:

    def __init__(self, color=LaTexColor.NavyBlue, language=PlannerLanguages.EN, font_family=FontFamily.SANS_SERIF,
                 start_week_monday=True):
        self.color = color
        self.font_family = font_family
        self.start_week_monday = start_week_monday
        self.t = language.value
        self.generate_calendar_sty()

    def generate_calendar_sty(self):
        with open('templates/calendar.sty', 'r') as file_template:
            template = Template(file_template.read())
            with open('calendar.sty', 'w') as file:
                day_keys = ['monday', 'tuesday', 'wednesday',
                            'thursday', 'friday', 'saturday', 'sunday']
                days = {k: v for k, v in zip(
                    day_keys, self.t['weekday'].values())}
                content = template.safe_substitute(days)
                file.write(content)

    def get_month(self, month_number: int):
        """
        Get month name based on month number (1-12 ~ Jan-Dec)
        Uses i18n reference for names
        :param month_number:
        :return:
        """
        return self.t['months'][month_number]

    def get_weekday(self, weekday_number: int):
        """
        Get weekday name based on number (0-6 ~ Mon-Sun)
        :param weekday_number:
        :return:
        """
        return self.t['weekday'][weekday_number]

    def create_calendar(self, year, month):
        """

        :param year:
        :param month:
        :return:
        """
        if self.start_week_monday:
            starting_day_number = 2  # Monday
        else:
            starting_day_number = 1  # Sunday

        var = Template("\\pagestyle{empty} % Removes the page number from the bottom of the page \n"
                       "\\noindent \n"
                       "\\StartingDayNumber=$starting_day_number"
                       " % Calendar starting day, default of 1 means Sunday, 2 for Monday, etc \n"
                       "%---------------------------------------------------------------------------------------- \n"
                       "%  MONTH AND YEAR SECTION \n"
                       "%---------------------------------------------------------------------------------------- \n"
                       "\\begin{center} \n"
                       "\\textsc{\\Huge \\color{$color}$month_name}\\\\ % Month \n"
                       "\\textsc{\\large $year} % Year \n"
                       "\\end{center} \n"
                       "%---------------------------------------------------------------------------------------- \n"
                       "\\begin{calendar}{11.7cm} \n").safe_substitute(
            {'color': self.color, 'starting_day_number': starting_day_number, 'year': year,
             'month_name': self.get_month(month)})
        weekday_begins, days_in_month = monthrange(year, month)
        for i in range(weekday_begins):
            var += "\\BlankDay \n"
        var += '%---------------------------------------------------------------------------------------- \n' \
               '% NUMBERED DAYS AND CALENDAR CONTENT \n' \
               '%---------------------------------------------------------------------------------------- \n\n' \
               '% These are the numbered days in the template - ' \
               'if there are less than 31 days simply comment out the bottom lines. \n\n' \
               '% \\vspace{2.5cm} is only there to provide an even look to the calendar' \
               ' where each day is 2.5cm tall, it can be changed or removed to automatically' \
               ' adjust to the day in the week with the most content \n\n' \
               '\\setcounter{calendardate}{1} % Start the date counter at 1 \n\n'
        for j in range(days_in_month):
            var += "\\day{}{\\vspace{1.5cm}} % " + str(j + 1) + " \n"
        var += '% Un-comment the \\BlankDay below if the bottom line of the calendar is missing \n' \
               '%\\BlankDay \n\n' \
               '%---------------------------------------------------------------------------------------- \n\n' \
               '\\finishCalendar \n' \
               '\\end{calendar} \n'
        return var

    def create_daily_pages(self, year, month):
        # Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for year, month.
        _weekday, days_in_month = monthrange(year, month)
        month_name = self.get_month(month)
        page: int = 1
        max_days_per_page = 4
        var = Template("{\\Huge $month_name} ~ {\\color{$color} \\large $year} \n "
                       "\\hfill \\break "
                       "\\hrule depth 0.3mm width \\hsize \\kern 1pt \\hrule width \\hsize height 0.2mm \n"
                       ).safe_substitute(month_name=month_name, color=self.color, year=year)
        for day in range(1, days_in_month + 1):
            weekday_name = self.get_weekday(date(year, month, day).weekday())
            if 0 != page % 2:
                # Left page
                template_page = Template("\\hfill \\break \\hfill \\break \n{\\Large $weekday_name} "
                                         "{\\LARGE\\color{$color} \\textbf{$day}}  \\hfill \\break"
                                         "\\hrule width \\hsize \\kern 2pt \\hfill \\break "
                                         "\\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \\break \n")
            else:
                # Right page
                template_page = Template("\\hfill \\break \n \\begin{flushright}{\\Large $weekday_name} "
                                         "{\\LARGE\\color{$color} \\textbf{$day}} \\end{flushright}"
                                         "\\hrule width \\hsize \\kern 2pt \\hfill \\break "
                                         "\\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \\break\n")
            var += template_page.safe_substitute(weekday_name=weekday_name,
                                                 color=self.color, day=day)

            if day % max_days_per_page == 0:
                # Add new page
                page += 1
                if 0 != page % 2:
                    # New left page
                    template_page = Template('\\newpage \\newgeometry{top=1cm, right=1.5cm,bottom=0.5cm, left=0.8cm} '
                                             '{\\Huge $month_name } ~ {\\color{$color} \\large $year} \n \\hfill '
                                             '\\break \\hrule depth 0.3mm width \\hsize \\kern 1pt '
                                             '\\hrule width \\hsize height 0.2mm \n')
                else:
                    template_page = Template('\\newpage \\newgeometry{top=1cm, left=1.5cm,bottom=0.5cm, right=0.8cm} '
                                             '\\begin{flushright} {\\Huge $month_name} ~ {\\color{$color} '
                                             '\\large $year} \\end{flushright} \n \\hrule depth 0.3mm width \\hsize '
                                             '\\kern 1pt \\hrule width \\hsize height 0.2mm \n')
                var += template_page.safe_substitute(month_name=month_name,
                                                     color=self.color, year=year)
        if 0 == page % 2:
            var += '\\afterpage{\\blankpage}'
        return var

    def personal_data(self):

        with open('templates/personal_data.tex', 'r') as personal_info_template:
            template = LaTexDelimiterTemplate(personal_info_template.read())
        return template.safe_substitute(self.t, color=self.color)

    def generate_annual_planner(self):
        with open('agenda.tex', 'w') as f:
            f.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n'
                    '% Annual Planner \n'
                    '% \n'
                    '% This template has been made by: \n'
                    '% Blanca Azucena Lopez Garduño (https://github.com/blankazucenalg/latex-agenda-planner) \n'
                    '% \n'
                    '% \n'
                    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n'
                    '% This template uses the '
                    '% Monthly Calendar LaTeX Template \n'
                    '% \n'
                    '% This template has been downloaded from: \n'
                    '% http://www.latextemplates.com \n'
                    '% Original calendar style author: \n'
                    '% Evan Sultanik (http://www.sultanik.com/LaTeX_calendar_style) \n'
                    '% \n'
                    '% Important note: \n'
                    '% This template requires the calendar.sty file to be in the same directory as the \n'
                    '% .tex file. The calendar.sty file provides the necessary structure to create the \n'
                    '% calendar. \n'
                    '% \n'
                    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n'
                    ' \n'
                    '%---------------------------------------------------------------------------------------- \n'
                    '%  PACKAGES AND OTHER DOCUMENT CONFIGURATIONS \n'
                    '%---------------------------------------------------------------------------------------- \n'
                    ' \n'
                    '\\documentclass[portrait]{article} \n'
                    ' \n'
                    '\\usepackage{calendar} % Use the calendar.sty style \n'
                    ' \n'
                    # paper size and margins
                    '\\usepackage[paperwidth=13.2cm, paperheight=19.5cm, top=0.5cm,'
                    ' left=1.5cm, bottom=0.5cm, right=0.8cm]{geometry} \n'
                    '\\usepackage{color} \n'
                    '\\usepackage[dvipsnames]{xcolor} \n'
                    '\\usepackage{ragged2e} \n'
                    '\\usepackage{afterpage} \n'
                    '\\newcommand\\blankpage{% \n'
                    '\\null \n'
                    '\\thispagestyle{empty}% \n'
                    '\\addtocounter{page}{-1}% \n'
                    '\\newpage} \n'
                    # font family
                    '\\renewcommand{\\familydefault}{\\' + \
                    str(self.font_family) + '}'
                                            '\\begin{document} \n')
            # Get current year
            year = date.today().year
            # Write first page with personal data
            f.write(self.personal_data())
            # Generate planner for twelve months
            for month in range(1, 13):
                f.write(
                    '\\newpage \\newgeometry{left=0.5cm,bottom=0.5cm,right=0.5cm,top=2.3in} \n')
                f.write(self.create_calendar(year, month))
                f.write(
                    '\\newpage \\restoregeometry \\newpage '
                    '\\newgeometry{top=1cm, right=1.5cm,bottom=0.5cm, left=0.8cm}')
                f.write(self.create_daily_pages(year, month))
            f.write('\\end{document} \n')


def main():
    # Fav colors: 'NavyBlue', 'Dandelion', 'RawSienna'
    planner = LaTexPlanner(color=LaTexColor.Dandelion,
                           language=PlannerLanguages.ES,
                           font_family=FontFamily.SANS_SERIF,
                           start_week_monday=True
                           )
    planner.generate_annual_planner()


if __name__ == '__main__':
    main()
