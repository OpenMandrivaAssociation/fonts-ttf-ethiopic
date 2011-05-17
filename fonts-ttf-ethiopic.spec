Summary:	Ethiopic TrueType fonts
Name:		fonts-ttf-ethiopic
Version:	1.0
Release:	%mkrel 12
License:	GPL
Group:		System/Fonts/True type
# GFZemen unicode font from
# ftp://ftp.ethiopic.org/pub/fonts/TrueType/gfzemenu.ttf
# the site seems gone now
Source0:	fonts-ttf-ethiopic.tar.bz2

BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	mkfontscale

%description
This Package provides Free Ethiopic TrueType fonts.

%prep

%setup -q -n %{name}

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/ethiopic/
cp *.ttf %buildroot/%_datadir/fonts/TTF/ethiopic/

(
cd %buildroot/%_datadir/fonts/TTF/ethiopic/
mkfontscale > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/ethiopic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/ethiopic/
%_datadir/fonts/TTF/ethiopic/*
%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50

