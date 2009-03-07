Summary:	Ethiopic TrueType fonts
Name:		fonts-ttf-ethiopic
Version:	1.0
Release:	%mkrel 8
License:	GPL
Group:		System/Fonts/True type
# GFZemen unicode font from
# ftp://ftp.ethiopic.org/pub/fonts/TrueType/gfzemenu.ttf
# the site seems gone now
Source0:	fonts-ttf-ethiopic.tar.bz2

BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

%description
This Package provides Free Ethiopic TrueType fonts.

%prep

%setup -q -n %{name}

%build

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/ethiopic/
cp *.ttf %buildroot/%_datadir/fonts/TTF/ethiopic/

(
cd %buildroot/%_datadir/fonts/TTF/ethiopic/
%_sbindir/ttmkfdir -u -m 1 > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/ethiopic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50

%post
[ -x %{_bindir}/fc-cache ]  && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %{_bindir}/fc-cache ]  && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%dir %_datadir/fonts/TTF/ethiopic/
%_datadir/fonts/TTF/ethiopic/*
%_sysconfdir/X11/fontpath.d/ttf-ethiopic:pri=50

