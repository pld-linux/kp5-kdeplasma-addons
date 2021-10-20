#
# Conditional build:
%bcond_without	qtwebengine	# build with Qt5Webengine support

%ifarch x32
%undefine	with_qtwebengine
%endif

%define		kdeplasmaver	5.23.1
%define		qtver		5.9.0
%define		kpname		kdeplasma-addons

Summary:	All kind of addons to improve your Plasma experience
Name:		kp5-%{kpname}
Version:	5.23.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	12fbadbb07c069e74d2e965408f4222a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
%{?with_qtwebengine:BuildRequires:	Qt5WebEngine-devel}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	glib2-devel
BuildRequires:	ibus-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesignerplugin-devel
BuildRequires:	kf5-kholidays-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kross-devel
BuildRequires:	kf5-kross-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kunitconversion-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
All kind of addons to improve your Plasma experience.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
		../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_datadir}/knsrcfiles/comic.knsrc
%ghost %{_libdir}/libplasmacomicprovidercore.so.1
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_applet_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_comic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_konsoleprofiles.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker/libcolorpickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/colorpicker/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/diskquota
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/diskquota/libdiskquotaplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/diskquota/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch/libquicklaunchplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/quicklaunch/qmldir

%dir %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/libfifteenpuzzleplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/fifteenpuzzle/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/notes
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/notes/libnotesplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/notes/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/timer
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/timer/libtimerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/timer/qmldir
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%dir %{_datadir}/kservices5/kwin
%{_datadir}/kservices5/kwin/kwin4_desktop_switcher_previews.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_big_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_compact.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_informative.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_present_windows.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_small_icons.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_text.desktop
%{_datadir}/kservices5/kwin/kwin4_window_switcher_thumbnails.desktop
%{_datadir}/kservices5/plasma-runner-dictionary_config.desktop
%{_datadir}/kservices5/plasma-runner-spellchecker_config.desktop
%dir %{_datadir}/kwin
%{_datadir}/kwin/desktoptabbox
%{_datadir}/kwin/tabbox
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.calculator
%{_datadir}/plasma/plasmoids/org.kde.plasma.comic
%{_datadir}/plasma/plasmoids/org.kde.plasma.fifteenpuzzle
%{_datadir}/plasma/plasmoids/org.kde.plasma.fuzzyclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/plasmoids/org.kde.plasma.konsoleprofiles
%{_datadir}/plasma/plasmoids/org.kde.plasma.notes
%{_datadir}/plasma/plasmoids/org.kde.plasma.timer
%{_datadir}/plasma/plasmoids/org.kde.plasma.diskquota
%{_datadir}/plasma/plasmoids/org.kde.plasma.quicklaunch
%{_datadir}/plasma/plasmoids/org.kde.plasma.userswitcher
%{_datadir}/plasma/services/org.kde.plasma.dataengine.konsoleprofiles.operations
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango

%{_libdir}/libplasmapotdprovidercore.so
%ghost %{_libdir}/libplasmapotdprovidercore.so.1
%{_libdir}/libplasmapotdprovidercore.so.1.*.*
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.grouping.so
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.private.grouping.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_weather.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_potd.so
%dir %{_libdir}/qt5/plugins/potd
%{_libdir}/qt5/plugins/potd/plasma_potd_apodprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_bingprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_epodprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_flickrprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_natgeoprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_noaaprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_unsplashprovider.so
%{_libdir}/qt5/plugins/potd/plasma_potd_wcpotdprovider.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/libmediaframeplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediaframe/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/purpose
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/libpurposeplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/purpose/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/weather
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/libweatherplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/weather/qmldir
%{_datadir}/metainfo/org.kde.haenau.appdata.xml
%{_datadir}/metainfo/org.kde.hunyango.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.activitypager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.binaryclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.calculator.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.colorpicker.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.comic.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.diskquota.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.fifteenpuzzle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.fuzzyclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.grouping.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kickerdash.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.konsoleprofiles.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mediaframe.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.notes.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicklaunch.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quickshare.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.timer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.userswitcher.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.weather.appdata.xml
%{_datadir}/metainfo/org.kde.potd.appdata.xml
%dir %{_datadir}/plasma/desktoptheme/default/weather
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitypager
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping
%{_datadir}/plasma/plasmoids/org.kde.plasma.quickshare
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather
%{_datadir}/plasma/wallpapers/org.kde.potd
%{_libdir}/qt5/plugins/kcm_krunner_charrunner.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents.so
%dir %{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents
%{_libdir}/qt5/plugins/plasmacalendarplugins/astronomicalevents/AstronomicalEventsConfig.qml
%dir %{_libdir}/qt5/qml/org/kde/plasmacalendar
%dir %{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig
%{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/libplasmacalendarastronomicaleventsconfig.so
%{_libdir}/qt5/qml/org/kde/plasmacalendar/astronomicaleventsconfig/qmldir
%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_datadir}/kservices5/plasma-runner-character_config.desktop
%{_datadir}/metainfo/org.kde.plasma.keyboardindicator.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator
%dir %{_libdir}/qt5/plugins/kf5/krunner
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_charrunner.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_datetime.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_katesessions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_konsoleprofiles.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_spellcheck.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/nightcolorcontrol
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/nightcolorcontrol/libnightcolorcontrolplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/nightcolorcontrol/qmldir
%{_datadir}/kservices5/kwin/kwin4_window_switcher_thumbnail_grid.desktop
%{_datadir}/metainfo/org.kde.plasma.nightcolorcontrol.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.nightcolorcontrol
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/unitconverter.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/plasma_comic.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_comic_krossprovider.so
%{_libdir}/qt5/qml/org/kde/plasma/private/dict/libdictplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/dict/qmldir
%{_iconsdir}/hicolor/scalable/apps/accessories-dictionary.svg*
%{_datadir}/metainfo/org.kde.plasma.webbrowser.appdata.xml
%{_datadir}/metainfo/org.kde.plasma_applet_dict.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict
%{_datadir}/qlogging-categories5/plasma_comic.categories

%if %{with qtwebengine}
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/plasma/potdprovider
%{_libdir}/cmake/PlasmaPotdProvider
