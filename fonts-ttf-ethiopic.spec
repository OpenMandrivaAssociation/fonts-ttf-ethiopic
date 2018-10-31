Summary:	Ethiopic TrueType fonts
Name:		fonts-ttf-ethiopic
Version:	1.0
Release:	24
License:	GPLv2
Group:		System/Fonts/True type
# GFZemen unicode font from
# ftp://ftp.ethiopic.org/pub/fonts/TrueType/gfzemenu.ttf
# the site seems gone now
Source0:	fonts-ttf-ethiopic.tar.bz2

BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale

%description
This Package provides Free Ethiopic TrueType fonts.

%prep
%setup -qn %{name}

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/ethiopic/
cp *.ttf %{buildroot}/%{_datadir}/fonts/TTF/ethiopic/

(
cd %{buildroot}/%{_datadir}/fonts/TTF/ethiopic/
mkfontscale > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/ethiopic \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-ethiopic:pri=50

%files
%dir %{_datadir}/fonts/TTF/ethiopic/
%{_datadir}/fonts/TTF/ethiopic/*
%{_sysconfdir}/X11/fontpath.d/ttf-ethiopic:pri=50

