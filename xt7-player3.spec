######################################################
# SpecFile: xt7-player3.spec
# For unstable branch do:
# git clone https://github.com/kokoko3k/xt7-player.git 
######################################################
%define oname xt7-player

Summary:	Xt7-player mplayer GUI
Name:		xt7-player3
Version:	3.3.7
Release:	2
URL:		http://xt7-player.sourceforge.net/xt7forum/
Source:		https://github.com/kokoko3k/xt7-player.git/%{oname}-src-%{version}.tar.gz
Source1:	%{oname}.desktop
License:	GPLv2
Group:		Video
BuildArch:	noarch
BuildRequires:	gambas3-runtime >= 3.3.4
BuildRequires:	gambas3-gb-qt4
BuildRequires:	gambas3-gb-form
BuildRequires:	gambas3-gb-desktop
BuildRequires:	gambas3-gb-form-mdi
BuildRequires:	gambas3-gb-net
BuildRequires:	gambas3-gb-net-curl
BuildRequires:	gambas3-gb-settings
BuildRequires:	gambas3-gb-xml
BuildRequires:	gambas3-gb-web
BuildRequires:	gambas3-devel >= 3.3.4
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
BuildRequires:	gambas3-gb-signal >= 3.3.4
# 4 desktop file check
BuildRequires:	desktop-file-utils

# 4 icons convert
BuildRequires:	imagemagick

# 4 dvb-epg
Requires:	dvbsnoop
Requires:	dvb-apps

# 4 downloading from youtube
Requires:	youtube-dl >= 2012.09.27
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
Requires:	gambas3-runtime >= 3.3.1
Requires:	gambas3-gb-image
Requires:	gambas3-gb-dbus
Requires:	gambas3-gb-qt4 >= 3.3.1
Requires:	gambas3-gb-gtk
Requires:	gambas3-gb-gui >= 3.3.1
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
Requires:	gambas3-gb-signal >= 3.3.4
Provides:	%{oname} == %{version}

%rename Xt7-player3

AutoReqProv:	no

%description
Xt7-Player, an (almost) complete mplayer GUI
This program is written in Gambas3, so you will need Gambas3 to be installed.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --prefix=/usr
%make

%install
%makeinstall
#icons
cd xt7-player 
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert xt7-player.png -resize 32x32 %{buildroot}%{_iconsdir}/%{oname}.png
convert xt7-player.png -resize 16x16 %{buildroot}%{_miconsdir}/%{oname}.png
install -p xt7-player.png %{buildroot}%{_liconsdir}/xt7-player.png

#menu entry
desktop-file-install %{SOURCE1} \
	--dir %{buildroot}%{_datadir}/applications


%files
%doc COPYING README ChangeLog INSTALL
%{_bindir}/*
%{_iconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_datadir}/applications/%{oname}.desktop

