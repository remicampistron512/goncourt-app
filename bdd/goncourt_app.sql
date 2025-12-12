-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 12 déc. 2025 à 12:44
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt_app`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `aut_id` int NOT NULL AUTO_INCREMENT,
  `aut_biography` text COLLATE utf8mb4_unicode_ci,
  `aut_last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `aut_first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`aut_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`aut_id`, `aut_biography`, `aut_last_name`, `aut_first_name`) VALUES
(1, NULL, 'Appanah', 'Nathacha'),
(2, NULL, 'Carrère', 'Emmanuel'),
(3, NULL, 'Deneufgermain', 'David'),
(4, NULL, 'Diop', 'David'),
(5, NULL, 'Dunant', 'Ghislaine'),
(6, NULL, 'Gasnier', 'Paul'),
(7, NULL, 'Lahens', 'Yanick'),
(8, NULL, 'Lamarche', 'Caroline'),
(9, NULL, 'Laurain', 'Hélène'),
(10, NULL, 'Majdalani', 'Charif'),
(11, NULL, 'Mauvignier', 'Laurent'),
(12, NULL, 'Montesquiou', 'Alfred de'),
(13, NULL, 'Poix', 'Guillaume'),
(14, NULL, 'Pourchet', 'Maria'),
(15, NULL, 'Thomas', 'David');

-- --------------------------------------------------------

--
-- Structure de la table `award_edition`
--

DROP TABLE IF EXISTS `award_edition`;
CREATE TABLE IF NOT EXISTS `award_edition` (
  `awa_id` int NOT NULL AUTO_INCREMENT,
  `awa_year` smallint NOT NULL,
  `awa_date` date DEFAULT NULL,
  `awa_location` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lit_id` int NOT NULL,
  PRIMARY KEY (`awa_id`),
  KEY `lit_id` (`lit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `award_edition`
--

INSERT INTO `award_edition` (`awa_id`, `awa_year`, `awa_date`, `awa_location`, `lit_id`) VALUES
(1, 2025, '2025-11-04', 'Paris', 1);

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `boo_id` int NOT NULL AUTO_INCREMENT,
  `boo_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `boo_summary` text COLLATE utf8mb4_unicode_ci,
  `boo_publishing_date` date DEFAULT NULL,
  `boo_nb_pages` smallint DEFAULT NULL,
  `boo_isbn` varchar(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  `boo_editor_price` decimal(5,2) DEFAULT NULL,
  `editr_id` int NOT NULL,
  `aut_id` int NOT NULL,
  PRIMARY KEY (`boo_id`),
  UNIQUE KEY `boo_isbn` (`boo_isbn`),
  KEY `editr_id` (`editr_id`),
  KEY `aut_id` (`aut_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO `book` (`boo_id`, `boo_title`, `boo_summary`, `boo_publishing_date`, `boo_nb_pages`, `boo_isbn`, `boo_editor_price`, `editr_id`, `aut_id`) VALUES
(1, 'La nuit au cœur', '« De ces nuits et de ces vies, de ces femmes qui courent, de ces coeurs qui luttent, de ces instants qui sont si accablants qu\'ils ne rentrent pas dans la mesure du temps, il a fallu faire quelque chose. Il y a l\'impossibilité de la vérité entière à chaque page mais la quête désespérée d\'une justesse au plus près de la vie, de la nuit, du coeur, du corps, de l\'esprit.\r\n\r\nDe ces trois femmes, il a fallu commencer par la première, celle qui vient d\'avoir vingt-cinq ans quand elle court et qui est la seule à être encore en vie aujourd\'hui.\r\n\r\nCette femme, c\'est moi. »\r\n\r\nLa nuit au coeur entrelace trois histoires de femmes victimes de la violence de leur compagnon. Sur le fil entre force et humilité, Nathacha Appanah scrute l\'énigme insupportable du féminicide conjugal, quand la nuit noire prend la place de l\'amour.', '2025-08-21', 288, '9782073080028', 21.00, 1, 1),
(2, 'Kolkhoze', 'Cette nuit-là, rassemblés tous les trois autour de notre mère, nous avons pour la dernière fois fait kolkhoze .', '2025-08-28', 558, '9782818061985', 24.00, 2, 2),
(3, 'L\'Adieu au visage', ' Un roman en apnée sur la pandémie. Ce qu\'elle a fait aux vivants et aux morts, à notre humanité.\r\n\r\nMars 2020. La France se confine. Dans tous les hôpitaux du pays, il faut prendre des décisions et agir vite. En première ligne, un psychiatre partage son temps entre son équipe mobile qui maraude dans une ville fantôme à la recherche de marginaux à protéger, et les unités covid où les malades meurent seuls, privés de tout rite. Entre obéissance à la loi et refus de l\'horreur, que ce soit à l\'hôpital ou dehors, chacun à son niveau cherche des solutions et improvise. L\'Adieu au visage est l\'écriture d\'une résistance fragile et d\'une lutte pour prendre soin de l\'autre.\r\n\r\n« Au commencement, on ne lave plus les corps, on ne les coiffe plus, on ne les habille plus, on ne les présente plus - d\'accompagner les morts, il n\'est plus question. »', '2025-08-20', 288, '9782381340647', 21.10, 3, 3),
(4, 'Où s\'adosse le ciel', 'À la fin du XIXe siècle, Bilal Seck achève un pèlerinage à La Mecque et s\'apprête à rentrer à Saint-Louis du Sénégal. Une épidémie de choléra décime alors la région, mais Bilal en réchappe, sous le regard incrédule d\'un médecin français qui cherche à percer les secrets de son immunité. En pure perte. Déjà, Bilal est ailleurs, porté par une autre histoire, celle qu\'il ne cesse de psalmodier, un mythe immense, demeuré intact en lui, transmis par la grande chaîne de la parole qui le relie à ses ancêtres. Une odyssée qui fut celle du peuple égyptien, alors sous le joug des Ptolémées, conduite par Ounifer, grand prêtre d\'Osiris qui caressait le rêve de rendre leur liberté aux siens, les menant vers l\'ouest à travers les déserts, jusqu\'à une terre promise, un bel horizon, là où s\'adosse le ciel...\r\nCe chemin, Bilal l\'emprunte à son tour, vers son pays natal, en passant par Djenné, la cité rouge, où vint buter un temps le voyage d\'Ounifer et de son peuple.\r\n\r\nDe l\'Égypte ancienne au Sénégal, David Diop signe un roman magistral sur un homme parti à la reconquête de ses origines et des sources immémoriales de sa parole. ', '2025-08-14', 368, '9782260057307', 22.50, 4, 4),
(5, 'Un amour infini', 'Première sélection duPrix Goncourt 2025.\r\n\r\nPremière sélection du prix Médicis 2025.\r\n\r\nUne parenthèse d\'une grâce absolue, qu\'on voudrait ne jamais refermer. Lire - Magazine littéraire\r\n\r\nElle est descendue en retard, elle voulait encore fumer une cigarette, fumer seule, une fois de plus. Pour sentir le temps qui passe, ne plus savoir qui elle est, ni ce qu\'on peut vouloir d\'elle.\r\n\r\nCe roman installe le lecteur au coeur d\'une rencontre de trois jours sur l\'île de Ténérife, en juin 1964, prévue mais bouleversée par un événement tragique, entre un astrophysicien d\'origine hongroise qui a dû fuir l\'Europe et s\'exiler aux États-Unis et une mère de famille française.\r\n\r\nAlors que rien ne devrait les rapprocher, leurs conversations sur leurs passés distincts et l\'exploration de l\'île vont les ouvrir profondément l\'un à l\'autre. Le ciel, l\'univers, l\'histoire de la Terre... Les sujets de l\'astrophysicien rejoignent la sensibilité de celle qui a observé le mystère de la toute petite enfance et a toujours eu une approche sensitive des êtres. Leur désir réciproque va s\'accompagner de la puissance des éléments qui les entourent.\r\n\r\n1964. Sur l\'île de Tenerife. Une femme et un homme que rien ne destinait à se rencontrer, et, pourtant, durant 3 jours, en cette géographie volcanique et insulaire, naîtra l\'une des plus belles rencontres amoureuses écrites ces dernières années...Roman sensible subtile et sensuel, où le paysage cosmique, absolu de l\'île de Tenerife et la rencontre entre Louise et Nathan confluent si intimement que l\'impression laissée par cette histoire à l\'écriture aussi délicate que tellurique perdure infiniment.\r\n\r\nKarine Henry - Librairie Comme Un roman', '2025-08-20', 170, '9782226498687', 19.90, 5, 5),
(6, 'La collision', 'En 2012, en plein centre-ville de Lyon, une femme décède brutalement, percutée par un jeune garçon en moto cross qui fait du rodéo urbain à 80 km/h.\r\n\r\nDix ans plus tard, son fils, qui n\'a cessé d\'être hanté par le drame, est devenu journaliste. Il observe la façon dont ce genre de catastrophe est utilisé quotidiennement pour fracturer la société et dresser une partie de l\'opinion contre l\'autre. Il décide de se replonger dans la complexité de cet accident, et de se lancer sur les traces du motard pour comprendre d\'où il vient, quel a été son parcours et comment un tel événement a été rendu possible.\r\n\r\nEn décortiquant ce drame familial, Paul Gasnier révèle deux destins qui s\'écrivent en parallèle, dans la même ville, et qui s\'ignorent jusqu\'au jour où ils entrent violemment en collision. C\'est aussi l\'histoire de deux familles qui racontent chacune l\'évolution du pays. Un récit en forme d\'enquête littéraire qui explore la force de nos convictions quand le réel les met à mal, et les manquements collectifs qui créent l\'irrémédiable.', '2025-08-21', 160, '9782073101228', 19.00, 1, 6),
(7, 'Passagères de nuit', 'Dans ce nouveau roman, comme arraché au chaos de son quotidien à Port-au-Prince, Yanick Lahens rend un hommage d’espoir et de résistance à la lignée des femmes dont elle est issue.\r\nLa première d’entre elles, Élizabeth Dubreuil, naît vers 1820 à La Nouvelle-Orléans. Sa grand-mère, arrivée d’Haïti au début du siècle dans le sillage du maître de la plantation qui avait fini par l’affranchir, n’a plus jamais voulu dépendre d’un homme. Inspirée par ce puissant exemple, la jeune Élisabeth se rebelle à son tour contre le désir prédateur d’un ami de son père. Elle doit fuir la ville, devenant à son tour une « passagère de nuit » sur un bateau à destination de Port-au-Prince. Ce qui adviendra d’elle, nous l’apprendrons quand son existence croisera celle de Régina, autre grande figure de ce roman des origines.\r\nNée pauvre parmi les pauvres dans un hameau du sud de l’île d’Haïti, Régina elle aussi a forcé le destin : rien ne la déterminait à devenir la maîtresse d’un des généraux arrivé en libérateur à Port-au-Prince en 1867. C’est à « mon général, mon amant, mon homme » qu’elle adresse le monologue amoureux dans lequel elle évoque sa trajectoire d’émancipation : la cruauté mesquine des maîtres qu’elle a fuis trouve son contrepoint dans les mains tendues par ces femmes qui lui ont appris à opposer aux coups du sort une ténacité silencieuse.\r\nCette ténacité silencieuse, Élizabeth et Régina l’ont reçue en partage de leurs lointaines ascendantes, ces « passagères de nuit » des bateaux négriers, dont Yanick Lahens évoque ici l’effroyable réalité, de même qu’elle nous plonge – et ce n’est pas la moindre qualité de ce très grand livre – dans les convulsions de l’histoire haïtienne.\r\nLorsque les deux héroïnes se rencontreront, dans une scène d’une rare qualité d’émotion, nous, lectrices et lecteurs, comprendrons que l’histoire ne s’écrit pas seulement avec les vainqueurs, mais dans la beauté des gestes, des regards et des mystères tus, qui à bas bruit montrent le chemin d’une résistance forçant l’admiration. ', '2025-08-28', 223, '9782848055701', 20.00, 6, 7),
(8, 'Le bel obscur', 'Alors qu’elle tente d’élucider le destin d’un ancêtre banni par sa famille, une femme reprend l’histoire de sa propre vie. Des années auparavant, son mari, son premier et grand amour, lui a révélé être homosexuel. Du bouleversement que ce fut dans leur existence comme des péripéties de leur émancipation respective, rien n’est tu. Ce roman lumineux nous offre une leçon de courage, de tolérance, de curiosité aussi. Car jamais cette femme libre n’aura cessé de se réinventer, d’affirmer la puissance de ses rêves contre les conventions sociales, avec une fantaisie et une délicatesse infinies.\r\n\r\nCaroline Lamarche vit à Liège. Son œuvre témoigne d’un éclectisme et d’une hardiesse renouvelés de livre en livre. Elle a notamment obtenu le prix Rossel avec Le Jour du Chien (Les Éditions de Minuit) et le Goncourt de la nouvelle pour Nous sommes à la lisière (Gallimard). Elle signe avec Le Bel Obscur son retour au roman. ', '2025-08-22', 240, '9782021603439', 20.00, 7, 8),
(9, 'Tambora', 'Une mère nous parle de ses deux filles, qu’elle voit amples comme des villes en expansion. La première est déjà là quand le récit commence, la seconde naîtra bientôt, après la perte d’un autre enfant lors d’une fausse couche. Ici, la temporalité de la maternité domine : celle de grossesses compliquées, d’hôpitaux et de services des urgences, la temporalité d’un corps qui produit, parfois sans qu’on le veuille, la temporalité de la naissance, celle des soins, ou des désirs trop souvent empêchés. Mais d’autres réalités existent aussi, se faufilent et tentent de prendre leur place : un manuscrit qui intéresse un éditeur, des confinements, qui ne changent pas grand-chose lorsqu’on doit rester alitée, la catastrophe environnementale qui se déploie, gigantesque, et fait songer à la fin du monde que l’humanité a cru vivre en 1815 quand l’éruption du volcan Tambora plongea une partie de la Terre dans le froid et l’obscurité. Hélène Laurain écrit avec cela, et écrit tout cela, avec crudité parfois. Son livre conjugue récit, réflexions et poésie, et nous emmène à la rencontre d’un monde incertain.', '2025-08-28', 192, '9782378562588', 18.50, 8, 9),
(10, 'Le nom des rois', '« Et d\'un seul coup, le monde qui servait de décor à tout cela s\'écroula. J\'en avais été un témoin distrait, mais le bruit qu\'il provoqua en s\'effondrant me fit lever la tête et ce que je vis alors n\'était plus qu\'un univers de violence et de mort. C\'est de celui-là que je suis devenu contemporain. J\'avais été, durant des années, dispensé d\'intérêt pour ce qui se passait autour de moi par ma passion des atlas, par les royautés anciennes et inutiles et par les terres lointaines et isolées, les berceaux de vieux empires oubliés.\r\n\r\nDésormais, l\'histoire se faisait sous mes yeux et je la trouvais moche, roturière et vulgaire. »\r\n\r\nDans ce récit de passage à l\'âge adulte porté par une écriture ample et élégante, Charif Majdalani raconte la disparition d\'un pays et explore ce qui subsiste de l\'enfance lorsqu\'elle capitule devant les fracas du monde.', '2025-08-20', 216, '9782234097278', 20.00, 9, 10),
(11, 'La maison vide', 'En 1976, mon père a rouvert la maison qu’il avait reçue de sa mère, restée fermée pendant vingt ans.\r\n\r\nÀ l’intérieur : un piano, une commode au marbre ébréché, une Légion d’honneur, des photographies sur lesquelles un visage a été découpé aux ciseaux.\r\n\r\nUne maison peuplée de récits, où se croisent deux guerres mondiales, la vie rurale de la première moitié du vingtième siècle, mais aussi Marguerite, ma grand-mère, sa mère Marie-Ernestine, la mère de celle-ci, et tous les hommes qui ont gravité autour d’elles.\r\n\r\nToutes et tous ont marqué la maison et ont été progressivement effacés. J’ai tenté de les ramener à la lumière pour comprendre ce qui a pu être leur histoire, et son ombre portée sur la nôtre.', '2025-08-28', 752, '9782707356741', 25.00, 10, 11),
(12, 'Le crépuscule des hommes', 'Chacun connaît les images du procès de Nuremberg, où Göring et vingt autres nazis sont jugés à partir de novembre 1945. Mais que se passe-t-il hors de la salle d\'audience ?\r\nIls sont là : Joseph Kessel, Elsa Triolet, Martha Gellhorn ou encore John Dos Passos, venus assister à ces dix mois où doit oeuvrer la justice. Des dortoirs de l\'étrange château Faber-Castell, qui loge la presse internationale, aux box des accusés, tous partagent la frénésie des reportages, les frictions entre alliés occidentaux et soviétiques, l\'effroi que suscite le récit inédit des déportés.\r\nAvec autant de précision historique que de tension romanesque, Alfred de Montesquiou ressuscite des hommes et des femmes de l\'ombre, témoins du procès le plus retentissant du XXe siècle. ', '2025-08-28', 384, '9782221267660', 22.00, 11, 12),
(13, 'Perpétuité', '18h45. Une maison d\'arrêt du sud de la France. Pierre, Houda, Laurent, Maëva et d\'autres surveillants prennent leur service de nuit. Captifs d\'une routine qui menace à chaque instant de déraper, ces agents de la pénitentiaire vont traverser ensemble une série d\'incidents plus éprouvants qu\'à l\'ordinaire.\r\n\r\nEn regardant celles et ceux qui regardent, Guillaume Poix plonge dans le quotidien d\'un métier méconnu, sinon méprisé, et interroge le sens d\'une institution au bord du gouffre.', '2025-08-21', 331, '9782073105455', 22.00, 12, 13),
(14, 'Tressaillir', '« J\'ai coupé un lien avec quelque chose d\'aussi étouffant que vital et je ne suis désormais plus branchée sur rien. Ni amour, ni foi, ni médecine. »\r\n\r\nUne femme est partie. Elle a quitté la maison, défait sa vie. Elle pensait découvrir une liberté neuve mais elle éprouve, prostrée dans une chambre d\'hôtel, l\'élémentaire supplice de l\'arrachement. Et si rompre n\'était pas à sa portée ? Si la seule issue au chagrin, c\'était revenir ? Car sans un homme à ses côtés, cette femme a peur. Depuis toujours sur le qui-vive, elle a peur.\r\n\r\nMais au fond, de quoi ?\r\n\r\nDans ce texte du retour aux origines et du retour de la joie, Maria Pourchet entreprend une archéologie de ces terreurs d\'enfant qui hantent les adultes. Elle nous transporte au coeur des forêts du Grand Est sur les traces de drames intimes et collectifs..', '2025-08-20', 324, '9782234097155', 21.90, 9, 14),
(15, 'Un frère', '« Pendant presque quarante ans, il aura été là sans plus vraiment être là. Lui, mais plus lui. Un autre. »\r\n\r\nDavid Thomas raconte le combat de son frère contre cette tyrannie intérieure qu’est la schizophrénie. Sa dureté, sa noirceur, ses ravages. Depuis la mort brutale d’Édouard jusqu’aux années heureuses, il remonte à la source du lien qu’il a eu avec son aîné et grâce auquel il s’est construit. Lors de ce cheminement, il s’interroge : comment écrire cette histoire sans trahir, sans enjoliver ? Écrire pour rejoindre Édouard. Le retrouver.\r\n\r\nDavid Thomas est l’auteur de plusieurs romans et recueils d’instantanés parmi lesquels La Patience des buffles sous la pluie ou Seul entouré de chiens qui mordent (prix de la nouvelle de l’Académie française 2021). Son dernier livre, Partout les autres , a été couronné en 2023 par le prix Goncourt de la nouvelle. ', '2025-08-22', 144, '9782823623376', 19.50, 13, 15);

-- --------------------------------------------------------

--
-- Structure de la table `character_`
--

DROP TABLE IF EXISTS `character_`;
CREATE TABLE IF NOT EXISTS `character_` (
  `cha_id` int NOT NULL AUTO_INCREMENT,
  `char_nickname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `cha_last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cha_first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `boo_id` int NOT NULL,
  PRIMARY KEY (`cha_id`),
  KEY `boo_id` (`boo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `character_`
--

INSERT INTO `character_` (`cha_id`, `char_nickname`, `cha_last_name`, `cha_first_name`, `boo_id`) VALUES
(1, 'Femme 1', '', '', 1),
(2, 'Femme 2', '', '', 1),
(3, 'mère de l\'auteur', '', '', 2),
(4, 'un psychiatre', '', '', 3),
(5, '', 'Seck', 'Bilal', 4),
(6, 'un astrophysicien d\'origine hongroise', '', '', 5),
(7, 'une mère de famille française', '', '', 5),
(8, 'Le fils d\'une femme décédée', '', '', 6),
(9, '', 'Dubreuil', 'Élizabeth ', 7),
(10, '', '', 'Régina', 7),
(11, 'une femme libre', '', '', 8),
(12, 'fille 1', '', '', 9),
(13, 'fille 2', '', '', 9),
(14, '', 'Majdalani', 'Charif ', 10),
(15, '', '', 'Marguerite', 11),
(16, '', '', 'Marie-Ernestine', 11),
(17, '', 'Kessel', 'Joseph ', 12),
(18, '', 'Triolet', 'Elsa', 12),
(19, '', 'Gellhorn', 'Martha ', 12),
(20, '', 'Dos Passos', 'John ', 12),
(21, '', '', 'Pierre', 13),
(22, '', '', 'Houda', 13),
(23, '', '', 'Laurent', 13),
(24, '', '', 'Maëva ', 13),
(25, 'Une femme', '', '', 14),
(26, '', 'Thomas', 'Édouard', 15);

-- --------------------------------------------------------

--
-- Structure de la table `contains`
--

DROP TABLE IF EXISTS `contains`;
CREATE TABLE IF NOT EXISTS `contains` (
  `cont_id` int NOT NULL AUTO_INCREMENT,
  `cont_fk_boo_id` int NOT NULL,
  `cont_fk_pha_id` int NOT NULL,
  PRIMARY KEY (`cont_id`),
  KEY `boo_id` (`cont_fk_boo_id`,`cont_fk_pha_id`) USING BTREE,
  KEY `contains_ibfk_2` (`cont_fk_pha_id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `contains`
--

INSERT INTO `contains` (`cont_id`, `cont_fk_boo_id`, `cont_fk_pha_id`) VALUES
(9, 1, 1),
(11, 2, 1),
(12, 3, 1),
(13, 4, 1),
(14, 5, 1),
(10, 6, 1),
(15, 7, 1),
(16, 8, 1),
(17, 9, 1),
(18, 10, 1),
(20, 11, 1),
(21, 12, 1),
(22, 13, 1),
(19, 14, 1),
(23, 15, 1);

-- --------------------------------------------------------

--
-- Structure de la table `editor`
--

DROP TABLE IF EXISTS `editor`;
CREATE TABLE IF NOT EXISTS `editor` (
  `editr_id` int NOT NULL AUTO_INCREMENT,
  `editr_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`editr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `editor`
--

INSERT INTO `editor` (`editr_id`, `editr_name`) VALUES
(1, 'Gallimard'),
(2, 'P.O.L'),
(3, 'Marchialy'),
(4, 'Julliard'),
(5, 'Albin Michel'),
(6, 'Sabine Wespieser'),
(7, 'Seuil'),
(8, 'Verdier'),
(9, 'Stock'),
(10, 'Minuit'),
(11, 'Robert Laffont'),
(12, 'Verticales'),
(13, 'L\'Olivier');

-- --------------------------------------------------------

--
-- Structure de la table `jury_member`
--

DROP TABLE IF EXISTS `jury_member`;
CREATE TABLE IF NOT EXISTS `jury_member` (
  `jur_id` int NOT NULL AUTO_INCREMENT,
  `jur_last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jur_first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jur_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `jur_login` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `jur_password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`jur_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `jury_member`
--

INSERT INTO `jury_member` (`jur_id`, `jur_last_name`, `jur_first_name`, `jur_type`, `jur_login`, `jur_password`) VALUES
(1, 'Didier', 'Decoin', 'Membre', '', ''),
(2, 'Angot', 'Christine', 'Membre', '', ''),
(3, 'Assouline', 'Pierre', 'Membre', '', ''),
(4, 'Ben Jelloun', 'Tahar', 'Membre', '', ''),
(5, 'Bruckner', 'Pascal', 'Membre', '', ''),
(6, 'Chandernagor', 'Françoise', 'Vice-présidente', '', ''),
(7, 'Claudel', 'Philippe', 'Président', '', ''),
(8, 'Constant', 'Paule', 'Membre', '', ''),
(9, 'Decoin', 'Didier', 'Membre', '', ''),
(10, 'Laurens', 'Camille', 'Membre', '', ''),
(11, 'Schmitt', 'Éric-Emmanuel', 'Membre', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `literary_award`
--

DROP TABLE IF EXISTS `literary_award`;
CREATE TABLE IF NOT EXISTS `literary_award` (
  `lit_id` int NOT NULL AUTO_INCREMENT,
  `lit_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`lit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `literary_award`
--

INSERT INTO `literary_award` (`lit_id`, `lit_name`) VALUES
(1, 'Prix Goncourt');

-- --------------------------------------------------------

--
-- Structure de la table `participate`
--

DROP TABLE IF EXISTS `participate`;
CREATE TABLE IF NOT EXISTS `participate` (
  `jur_id` int NOT NULL,
  `awa_id` int NOT NULL,
  PRIMARY KEY (`jur_id`,`awa_id`),
  KEY `awa_id` (`awa_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `phase`
--

DROP TABLE IF EXISTS `phase`;
CREATE TABLE IF NOT EXISTS `phase` (
  `pha_id` int NOT NULL AUTO_INCREMENT,
  `pha_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pha_date` date DEFAULT NULL,
  `pha_nb_books` int NOT NULL,
  `awa_id` int NOT NULL,
  PRIMARY KEY (`pha_id`),
  KEY `awa_id` (`awa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `phase`
--

INSERT INTO `phase` (`pha_id`, `pha_type`, `pha_date`, `pha_nb_books`, `awa_id`) VALUES
(1, 'Première sélection', '2025-09-03', 15, 1),
(2, 'Deuxième sélection', '2025-10-07', 8, 1),
(3, 'Troisième sélection', '2025-12-28', 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

DROP TABLE IF EXISTS `vote`;
CREATE TABLE IF NOT EXISTS `vote` (
  `vot_id` int NOT NULL AUTO_INCREMENT,
  `vot_nb_votes` int NOT NULL,
  `vot_fk_mem_id` int NOT NULL,
  `vot_fk_pha_id` int NOT NULL,
  `vot_fk_boo_id` int NOT NULL,
  PRIMARY KEY (`vot_id`),
  KEY `jur_id` (`vot_fk_mem_id`),
  KEY `pha_id` (`vot_fk_pha_id`),
  KEY `boo_id` (`vot_fk_boo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
