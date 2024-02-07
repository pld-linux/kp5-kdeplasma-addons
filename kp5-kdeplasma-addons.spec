#
# Conditional build:
%bcond_without	qtwebengine	# build with Qt6Webengine support
%bcond_with	tests		# build with tests

%ifarch x32
%undefine	with_qtwebengine
%endif

%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kpname		kdeplasma-addons

Summary:	All kind of addons to improve your Plasma experience
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	36f6a233949f9100f5e28aa1aea6f351
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
%{?with_qtwebengine:BuildRequires:	Qt6WebEngine-devel}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	glib2-devel
BuildRequires:	ibus-devel
BuildRequires:	kf6-karchive-devel
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kholidays-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-knewstuff-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-kparts-devel
BuildRequires:	kf6-krunner-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-kunitconversion-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

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
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/colorpicker
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/colorpicker/libcolorpickerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/colorpicker/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/diskquota
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/diskquota/libdiskquotaplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/diskquota/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/quicklaunch
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/quicklaunch/libquicklaunchplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/quicklaunch/qmldir

%dir %{_libdir}/qt6/qml/org/kde/plasma/private/fifteenpuzzle
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/fifteenpuzzle/libfifteenpuzzleplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/fifteenpuzzle/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/notes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/notes/libnotesplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/notes/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/timer
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/timer/libtimerplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/timer/qmldir
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%dir %{_datadir}/kwin
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
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango

%{_libdir}/libplasmapotdprovidercore.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.grouping.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.private.grouping.so
%dir %{_libdir}/qt6/plugins/potd
%{_libdir}/qt6/plugins/potd/plasma_potd_apodprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_bingprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_epodprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_flickrprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_natgeoprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_noaaprovider.so
%{_libdir}/qt6/plugins/potd/plasma_potd_wcpotdprovider.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mediaframe
%{_libdir}/qt6/qml/org/kde/plasma/private/mediaframe/libmediaframeplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mediaframe/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/weather
%{_libdir}/qt6/qml/org/kde/plasma/private/weather/libweatherplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/weather/qmldir
%{_datadir}/metainfo/org.kde.haenau.appdata.xml
%{_datadir}/metainfo/org.kde.hunyango.appdata.xml
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
%{_datadir}/metainfo/org.kde.plasma.timer.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.userswitcher.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.weather.appdata.xml
%{_datadir}/metainfo/org.kde.potd.appdata.xml
%dir %{_datadir}/plasma/desktoptheme/default/weather
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.binaryclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.grouping
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediaframe
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.grouping
%{_datadir}/plasma/plasmoids/org.kde.plasma.weather
%{_datadir}/plasma/wallpapers/org.kde.potd
%{_libdir}/qt6/plugins/plasmacalendarplugins/astronomicalevents.so
%dir %{_libdir}/qt6/plugins/plasmacalendarplugins/astronomicalevents
%{_libdir}/qt6/plugins/plasmacalendarplugins/astronomicalevents/AstronomicalEventsConfig.qml
%dir %{_libdir}/qt6/qml/org/kde/plasmacalendar
%dir %{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/libplasmacalendarastronomicaleventsconfig.so
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/qmldir
%{_datadir}/metainfo/org.kde.plasma.keyboardindicator.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.colorpicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardindicator
%dir %{_libdir}/qt6/plugins/kf6/krunner
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_charrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_katesessions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_konsoleprofiles.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/krunner_spellcheck.so
%{_libdir}/qt6/plugins/kf6/krunner/org.kde.datetime.so

%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/unitconverter.so

%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_charrunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_dictionary.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/krunner/kcms/kcm_krunner_spellcheck.so
%attr(755,root,root) %{_libdir}/qt6/plugins/potd/plasma_potd_simonstalenhagprovider.so

%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.weather.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/potd
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/potd/libplasma_wallpaper_potdplugin.so
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/wallpapers/potd/qmldir

%{_libdir}/qt6/plugins/plasmacalendarplugins/alternatecalendar.so
%dir %{_libdir}/qt6/plugins/plasmacalendarplugins/alternatecalendar
%{_libdir}/qt6/plugins/plasmacalendarplugins/alternatecalendar/AlternateCalendarConfig.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/profiles/libprofiles_qml_plugin.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/profiles
%{_libdir}/qt6/qml/org/kde/plasma/private/profiles/qmldir
%{_libdir}/qt6/qml/org/kde/plasmacalendar/alternatecalendarconfig/libplasmacalendaralternatecalendarconfig.so
%dir %{_libdir}/qt6/qml/org/kde/plasmacalendar/alternatecalendarconfig
%{_libdir}/qt6/qml/org/kde/plasmacalendar/alternatecalendarconfig/qmldir
%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2
%{_datadir}/metainfo/org.kde.plasma.addons.katesessions.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/contents/ui/KateSessionsItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.addons.katesessions/metadata.json

%ghost %{_libdir}/libplasmapotdprovidercore.so.2
%attr(755,root,root) %{_libdir}/libplasmapotdprovidercore.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_comic.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_cube_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.comic.so
%{_libdir}/qt6/qml/org/kde/plasma/private/colorpicker/colorpickerplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/colorpicker/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/dict/dictplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/dict/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/diskquota/diskquotaplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/diskquota/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/fifteenpuzzle/fifteenpuzzleplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/fifteenpuzzle/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mediaframe/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mediaframe/mediaframeplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/notes/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/notes/notesplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/profiles/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/profiles/profiles_qml_plugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/quicklaunch/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/quicklaunch/quicklaunchplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/timer/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/timer/timerplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/weather/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/weather/weatherplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/wallpapers/potd/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/wallpapers/potd/plasma_wallpaper_potdplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasmacalendar/alternatecalendarconfig/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasmacalendar/alternatecalendarconfig/plasmacalendaralternatecalendarconfig.qmltypes
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasmacalendar/astronomicaleventsconfig/plasmacalendarastronomicaleventsconfig.qmltypes
%{_datadir}/knotifications6/plasma_applet_timer.notifyrc
%{_datadir}/kwin/effects/cube/contents/config/main.xml
%{_datadir}/kwin/effects/cube/contents/ui/Cube.qml
%{_datadir}/kwin/effects/cube/contents/ui/CubeCameraController.qml
%{_datadir}/kwin/effects/cube/contents/ui/CubeFace.qml
%{_datadir}/kwin/effects/cube/contents/ui/DesktopView.qml
%{_datadir}/kwin/effects/cube/contents/ui/ScreenView.qml
%{_datadir}/kwin/effects/cube/contents/ui/constants.js
%{_datadir}/kwin/effects/cube/contents/ui/main.qml
%{_datadir}/kwin/effects/cube/metadata.json
%{_datadir}/qlogging-categories6/kdeplasma-addons.categories

%if %{with qtwebengine}
%{_datadir}/plasma/plasmoids/org.kde.plasma.webbrowser
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/dict
%{_libdir}/qt6/qml/org/kde/plasma/private/dict/libdictplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/dict/qmldir
%{_iconsdir}/hicolor/scalable/apps/accessories-dictionary.svg*
%{_datadir}/metainfo/org.kde.plasma.webbrowser.appdata.xml
%{_datadir}/metainfo/org.kde.plasma_applet_dict.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma_applet_dict
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/plasma/potdprovider
%{_libdir}/cmake/PlasmaPotdProvider
