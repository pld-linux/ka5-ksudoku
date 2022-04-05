#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		ksudoku
Summary:	ksudoku
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7d7c2bc6bf2d90d73ad65fec15e78c2f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5OpenGL-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSudoku is a logic-based symbol placement puzzle. The player has to
fill a grid so that each column, row as well as each square block on
the game field contains only one instance of each symbol.

%description -l pl.UTF-8
KSudoku jest grą logiczną. Gracz musi wypełnić planszę, tak żeby
każda kolumna, każdy wiersz i każdy kwadrat zawierał tylko jedno
wystąpienie danego symbolu.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ksudokurc
%attr(755,root,root) %{_bindir}/ksudoku
%{_desktopdir}/org.kde.ksudoku.desktop
%{_iconsdir}/hicolor/128x128/apps/ksudoku.png
%{_iconsdir}/hicolor/16x16/apps/ksudoku.png
%{_iconsdir}/hicolor/32x32/apps/ksudoku.png
%{_datadir}/ksudoku
%dir %{_datadir}/kxmlgui5/ksudoku
%{_datadir}/kxmlgui5/ksudoku/ksudokuui.rc
%{_datadir}/metainfo/org.kde.ksudoku.appdata.xml
