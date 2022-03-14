# 照片 加在h1(name)后面
# <div style="height: 260px; width: 170px;"><img alt="" src="./assets/profile.jpg" style="height: auto; max-width: 100%;" /></div>
# 打印样式 div-style 加上 float:right;

from tkinter.messagebox import NO


content = {
    "name": '''Chosen(Chen) Qiu <div style="height: 260px; width: 170px; float:right"><img alt="" src="./assets/profile.jpg" style="height: auto; max-width: 100%;" /></div>''',
    "title": "Chosen's Resume",

    "extra_style": "en_us.css",

    "profile": [
        {
            "src": "assets/email-logo.svg",
            "alt": "Email",
            "content": "chosenqiuch@gmail.com",
            "url": "mailto:chosenqiuch@gmail.com"
        },
    ],


    "sections": [
        {
            "title": "Introduction",
            "list": [
                {   "title": None,
                    "title_plain": None,
                    "content": '''
                        <p>
                            I am an undergratuate in School of physics and Astronomy at SYSU. My interest and research goal is solving real-world problems with
                            sundry technology. Among all technology I have acquired, I found Machine Leaning most charming and promising. 
                            I learnt most of my Machine Learning knowledge from online courses(thanks to Youtube, Coursera and Bilibili) and research practices.
                            With my knowledge in Physics, Mathematic, Computer Science and Machine Learning, I successfully developed a variety of models in galaxy images analysing.
                            Currently, I am working on project that using CNN to do structural decomposition in 2-component galaxies and writing my first paper on this.
                            In the future, I am looking forward to participating in more Machine Learning researches on image analyse, NLP or other area that will accutually make contribution to our world.  
                        </p>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Education experience",
            "list": [
                {

                    "logo_src": "assets/sysu-logo.svg",
                    "logo_alt": "Sun Yat-sen University Logo",

                    "title": "Sun Yat-sen University, Guangdong, China (Undergraduate)",
                    "title_plain": None,

                    "period": "08/2019 - Present",

                    "content": '''
                        <p>
                            Major: Physics        (GPA 3.55 / 4.00) <br>
                            Core crouses: Probability and Statistics, Linear Algebra, <br> 
                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; C Programming and data structure,Machine Learning and Python Practice, Mathematical Physics Methods <br>
                            Anticipated graduation date: 06/2023, <br>
                            
                        </p>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Professional Experience",
            "list": [
                {
                    #"logo_src": "assets/csst-logo.svg",
                    "logo_src": None,
                    "logo_alt": "CSST Logo",

                    "title": "Chinese Space Station Telescope (CSST), China",
                    "title_plain": None,

                    "period": "06/2020 - Present",

                    "content": '''
                        <p>
                            Technical researcher.
                        </p>
                        <p>
                            Developed a machine learning system Galaxy Light profile convolutional neural Networks (GaLNets)
                            using Convolutional Neural Network(CNN) to process the galaxy images to 
                            derive structural parameters on 1-Sersic model[GaLNets.I.] 
                            and perform Bulge-Disk on decomposition on 2-Sersic model[GaLNets.Ⅱ.]
                        </p>
                        <p>
                            Our system is now the fast and most accurate model in galaxy images analysing.  :)
                        </p>
                    ''',
                    "content_plain": None
                },
                {
                    "logo_src": None,
                    "logo_alt": None,

                    "title": "Media Center of Sun Yet-sun University",
                    "title_plain": None,

                    "period": "2020 - 2021",

                    "content": '''
                        <p>
                            Chairman.
                        </p>
                        <p>
                            Lead and organize media center in advertising our university.
                        </p>
                    ''',
                    "content_plain": None
                },
            ]
        },
        {
            "title": "Skill and Interests",
            "list": [
                {
                    "title": None,
                    "content": '''
                        <ul>
                            <li><p>
                                Mathematical and Physic basis and Computer Science Basis
                            </p></li>
                            <li><p>
                                Multiple scientific research tools: E.g. Matlab, TensorFlow, Topcat…
                            </p></li>
                            <li><p>
                                Machine learning knowledge in Image Processing, NLP…
                            </p></li>
                            <li><p>
                                Prefer using language: Python, C
                            </p></li>
                        </ul>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Research experience",
            "list": [
                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": 'Group lead by Nicola R. Napolitano',
                    "title_plain": None,

                    "period": None,

                    "content": '''
                        <p><i>(<a href="https://scholar.google.com/citations?hl=zh-CN&user=Z9klav0AAAAJ">https://scholar.google.com/citations?hl=zh-CN&user=Z9klav0AAAAJ</a>)</i></p>
                        <p>Researcher. We developed GaLNets with 
                        machine learning technique to enhance the 
                        performance of galaxy image processing in 
                        KiDs, CSST… </p>
                        
                    ''',
                    "content_plain": None
                },
            ]
        },
        {
            "title": "Selected awards",
            "list": [
                {

                    "logo_src": None,
                    "logo_alt": "Sysu",

                    "title": '''1. Scholarship''',
                    "title_plain": None,

                    "period": "2019 - 2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": "MathorCup",

                    "title": '''2. MathorCup Mathematical Modeling Tournament / Third Award''',
                    "title_plain": None,

                    "period": "2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": "APMCM",

                    "title": '''3. APMCM Mathematical Modeling Tournament / First Award''',
                    "title_plain": None,

                    "period": "2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
            ]
        },
        {
            "title": "Work published",
            "list": [

                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": '''1. GAlaxy Light profile convolutional neural NETworks (GaLNets). I. fast and accurate structural parameters for billion galaxy samples''',
                    "title_plain": None,

                    "period": None,

                    "content": '''<p><i>(<a href="https://arxiv.org/abs/2111.05434" alt="">https://arxiv.org/abs/2111.05434</a>)</i></p>''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": '''2. GAlaxy Light profile convolutional neural NETworks (GaLNets).Ⅱ. Bulge-Disk decomposition for deeper galaxy image in CSST''',
                    "title_plain": None,

                    "period": None,

                    "content": '''<p><i>(on the way)</i></p>''',
                    "content_plain": None
                },
            ]
        },
    ]
}
