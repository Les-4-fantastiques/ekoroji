-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Lun 27 Février 2023 à 16:43
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `ekoroji_bdd`
--

-- --------------------------------------------------------

--
-- Structure de la table `materiaux`
--

CREATE TABLE IF NOT EXISTS `materiaux` (
`id_materiau` int(11) NOT NULL,
  `nom_materiau` text NOT NULL,
  `est_reutilisable` tinyint(1) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Contenu de la table `materiaux`
--

INSERT INTO `materiaux` (`id_materiau`, `nom_materiau`, `est_reutilisable`) VALUES
(1, 'Carton', 1),
(2, 'Papier', 1),
(3, 'Fer', 1),
(4, 'Plastique', 0),
(5, 'Cuivre', 1),
(6, 'Zinc', 1),
(7, 'Aluminium', 1),
(8, 'Or', 1),
(9, 'Argent', 1),
(10, 'Plomb', 1),
(11, 'Bois', 1),
(12, 'Pétrole', 0),
(13, 'Acier', 1),
(14, 'Verre d''emballage', 1),
(15, 'Verre en verre', 0);

-- --------------------------------------------------------

--
-- Structure de la table `options_recyclage`
--

CREATE TABLE IF NOT EXISTS `options_recyclage` (
`id_option_recyclage` int(11) NOT NULL,
  `nom_option_recyclage` text NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Contenu de la table `options_recyclage`
--

INSERT INTO `options_recyclage` (`id_option_recyclage`, `nom_option_recyclage`) VALUES
(1, 'Poubelle jaune'),
(2, 'Usine de recyclage'),
(3, 'Poubelle verte'),
(4, 'Décharge'),
(5, 'Déchèterie'),
(6, 'Bacs à verres');

-- --------------------------------------------------------

--
-- Structure de la table `provenance`
--

CREATE TABLE IF NOT EXISTS `provenance` (
`id_provenance` int(11) NOT NULL,
  `nom_provenance` text NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Contenu de la table `provenance`
--

INSERT INTO `provenance` (`id_provenance`, `nom_provenance`) VALUES
(1, 'Chine'),
(2, 'États Unis'),
(3, 'Japon'),
(4, 'Australie'),
(5, 'Brésil'),
(6, 'Inde'),
(7, 'Europe'),
(8, 'Chili'),
(9, 'Mexico'),
(10, 'Canada'),
(11, 'Russie'),
(12, 'Moyen-Orient');

-- --------------------------------------------------------

--
-- Structure de la table `provenance_materiau`
--

CREATE TABLE IF NOT EXISTS `provenance_materiau` (
`id_provenance_materiau` int(11) NOT NULL,
  `id_materiau` int(11) NOT NULL,
  `id_provenance` int(11) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=35 ;

--
-- Contenu de la table `provenance_materiau`
--

INSERT INTO `provenance_materiau` (`id_provenance_materiau`, `id_materiau`, `id_provenance`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 1),
(5, 2, 2),
(6, 2, 3),
(7, 3, 1),
(8, 3, 4),
(9, 3, 5),
(10, 3, 6),
(11, 4, 1),
(12, 4, 2),
(13, 4, 7),
(14, 5, 8),
(15, 6, 1),
(16, 7, 1),
(17, 8, 1),
(18, 9, 9),
(19, 10, 1),
(20, 11, 2),
(21, 11, 10),
(22, 11, 11),
(23, 12, 11),
(24, 12, 2),
(25, 12, 12),
(26, 13, 6),
(27, 13, 2),
(28, 13, 11),
(29, 14, 1),
(30, 14, 7),
(31, 13, 2),
(32, 14, 1),
(33, 14, 7),
(34, 14, 2);

-- --------------------------------------------------------

--
-- Structure de la table `recyclage_materiau`
--

CREATE TABLE IF NOT EXISTS `recyclage_materiau` (
`id_recyclage_materiau` int(11) NOT NULL,
  `id_materiau` int(11) NOT NULL,
  `id_option_recyclage` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Contenu de la table `recyclage_materiau`
--

INSERT INTO `recyclage_materiau` (`id_recyclage_materiau`, `id_materiau`, `id_option_recyclage`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 3),
(5, 5, 2),
(6, 6, 2),
(7, 7, 2),
(8, 8, 2),
(9, 9, 2),
(10, 10, 2),
(11, 11, 4),
(12, 12, 5),
(13, 13, 4),
(14, 14, 6),
(15, 15, 14);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `materiaux`
--
ALTER TABLE `materiaux`
 ADD PRIMARY KEY (`id_materiau`);

--
-- Index pour la table `options_recyclage`
--
ALTER TABLE `options_recyclage`
 ADD PRIMARY KEY (`id_option_recyclage`);

--
-- Index pour la table `provenance`
--
ALTER TABLE `provenance`
 ADD PRIMARY KEY (`id_provenance`);

--
-- Index pour la table `provenance_materiau`
--
ALTER TABLE `provenance_materiau`
 ADD PRIMARY KEY (`id_provenance_materiau`);

--
-- Index pour la table `recyclage_materiau`
--
ALTER TABLE `recyclage_materiau`
 ADD PRIMARY KEY (`id_recyclage_materiau`), ADD KEY `id_recyclage_materiau_index` (`id_recyclage_materiau`), ADD KEY `id_option_recyclage_index` (`id_option_recyclage`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `materiaux`
--
ALTER TABLE `materiaux`
MODIFY `id_materiau` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `options_recyclage`
--
ALTER TABLE `options_recyclage`
MODIFY `id_option_recyclage` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT pour la table `provenance`
--
ALTER TABLE `provenance`
MODIFY `id_provenance` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT pour la table `provenance_materiau`
--
ALTER TABLE `provenance_materiau`
MODIFY `id_provenance_materiau` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=35;
--
-- AUTO_INCREMENT pour la table `recyclage_materiau`
--
ALTER TABLE `recyclage_materiau`
MODIFY `id_recyclage_materiau` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=16;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
