Summary:	Ethiopic TrueType fonts
Name:		fonts-ttf-ethiopic
Version:	1.0
Release:	%mkrel 15
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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-13mdv2011.0
+ Revision: 675416
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-12
+ Revision: 675180
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-11
+ Revision: 664328
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 1.0-10mdv2011.0
+ Revision: 605814
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-9mdv2010.1
+ Revision: 494139
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-8mdv2009.1
+ Revision: 351074
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 220862
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2008.1
+ Revision: 170836
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2008.1
+ Revision: 149796
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-4mdv2008.0
+ Revision: 48741
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:11:03 (52887)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:02:14 (52801)
- import fonts-ttf-ethiopic-1.0-2mdk

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0-2mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

