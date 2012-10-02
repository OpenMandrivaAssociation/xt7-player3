######################################################
# SpecFile: xt7-player3.spec
# git clone https://github.com/kokoko3k/xt7-player.git 
# git pull https://github.com/kokoko3k/xt7-player.git
######################################################

%define debug_package	%{nil}

######
%define oname xt7-player

Summary:	Xt7-player mplayer gui
Name:		xt7-player3
Version:	3.1.5
Release:	6
URL:		http://xt7-player.sourceforge.net/xt7forum/index.php
# git
Source:		https://github.com/kokoko3k/xt7-player.git/%{oname}.tar.gz
# stable
#Source:	http://wpage.unina.it/aorefice/xt7player_dist/%{oname}-src-%{version}.tar.gz
License:	GPLv2
Group:		Video
BuildArch:	noarch
BuildRequires:	gambas3-runtime >= 3.1.1
BuildRequires:	gambas3-gb-qt4
BuildRequires:	gambas3-gb-form
BuildRequires:	gambas3-gb-desktop
BuildRequires:	gambas3-gb-form-mdi
BuildRequires:	gambas3-gb-net
BuildRequires:	gambas3-gb-net-curl
BuildRequires:	gambas3-gb-settings
BuildRequires:	gambas3-gb-xml
BuildRequires:	gambas3-gb-web
BuildRequires:	gambas3-devel >= 3.1.1
BuildRequires:	gambas3-gb-image
BuildRequires:	gambas3-gb-image-imlib
BuildRequires:	gambas3-gb-image-io
BuildRequires:	gambas3-gb-db
BuildRequires:	gambas3-gb-dbus
BuildRequires:	gambas3-gb-db-form
BuildRequires:	gambas3-gb-qt4-ext
BuildRequires:	pkgconfig(taglib)
BuildRequires:	gambas3-gb-gui
BuildRequires:	gambas3-gb-compress
BuildRequires:	gambas3-gb-form-dialog

# 4 desktop file check
BuildRequires:	desktop-file-utils

# 4 icons convert
BuildRequires:	imagemagick

# 4 dvb-epg
Requires:	dvbsnoop
Requires:	dvb-apps

# 4 downloading from youtube
Requires:	youtube-dl
Requires:	xterm
Requires:	wget

# 4 subtiles , manage, download a.s.o.
Requires:	python >= 2.7

# 4 global hotkeys support
Requires:	xbindkeys

# 4 desktop integration
Requires:	xdg-utils

# 4 tagging
Requires:	%{_lib}taglib1
Requires:	%{_lib}taglib_c0

# default player, works also with mplayer2
Requires:	mplayer

# 4 GUI
Requires:	gambas3-runtime >= 3.1.1
Requires:	gambas3-gb-image
Requires:	gambas3-gb-dbus
Requires:	gambas3-gb-qt4 >= 3.1.1
Requires:	gambas3-gb-gtk
Requires:	gambas3-gb-gui >= 3.1.1
Requires:	gambas3-gb-form
Requires:	gambas3-gb-xml
Requires:	gambas3-gb-qt4-ext
Requires:	gambas3-gb-form-stock
Requires:	gambas3-gb-net
Requires:	gambas3-gb-form-dialog
Requires:	gambas3-gb-settings
Requires:	gambas3-gb-form-mdi
Requires:	gambas3-gb-compress
Requires:	gambas3-gb-desktop
Requires:	gambas3-gb-web
Requires:	gambas3-gb-net-curl
Provides:	%{oname} == %{version}

%rename Xt7-player3

AutoReqProv:	no

%description
Xt7-Player, an (almost) complete mplayer gui
This program is written in Gambas3, so you will need Gambas3 to be installed.

%prep
# stable
# setup -q -n %{oname}-%{version}

#git
%setup -q -n %{oname}

%build
# stable
#configure
#make

# git
gbc3 -e -a -g -t -p -m
gba3

%install
# stable
#cd xt7-player

# git && stable
#bin
install -d %{buildroot}%{_bindir}
install -p xt7-player.gambas %{buildroot}%{_bindir}/xt7-player

#icons
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert xt7-player.png -resize 32x32 %{buildroot}%{_iconsdir}/%{oname}.png
convert xt7-player.png -resize 16x16 %{buildroot}%{_miconsdir}/%{oname}.png
install -p xt7-player.png %{buildroot}%{_liconsdir}/xt7-player.png

#menu entry
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{oname}.desktop
[Desktop Entry]
Name=xt7-player
Comment=Xt7-Player, an (almost) complete mplayer gui
Exec=xt7-player
Icon=xt7-player
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/%{oname}.desktop

# stable
#cd ..

%files
# stable
#doc ChangeLog AUTHORS COPYING README
# git
%doc COPYING README CHANGELOG_GIT AA_ToDo
%{_bindir}/xt7-player
%{_miconsdir}/xt7-player.png
%{_iconsdir}/xt7-player.png
%{_liconsdir}/xt7-player.png
%{_datadir}/applications/%{oname}.desktop

