%define	name	clanbomber2
%define	version	0.9.1
%define	release	%mkrel 13
%define	Summary	Clanbomber - free (GPL) Bomberman-like multiplayer game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://www.clanbomber.de/files/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0: fusionsound_new_api.patch
Patch8:		clanbomber-1.02a-gcc-3.3.patch
Patch12:	clanbomber2-0.9-x86_64.patch
URL:		http://clanbomber.sourceforge.net/
License:	GPLv2+
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel libhermes-devel
BuildRequires:	libmikmod-devel libclanlib-sound automake >= 1.7
BuildRequires:	libfusionsound-devel

%description
ClanBomber is a free (GPL) Bomberman-like multiplayer game that uses ClanLib, a
free multi platform C++ game SDK. First "ClanBomber" was only a working title
for a small game started in September 1998, that has only been started to learn
how to use ClanLib. But the ClanBomber project has grown into a real game. It
is fully playable and features Computer controlled bombers, however, it is
recommended to play ClanBomber with friends (3-8 players are really fun).

Clanbomber2 is a port of ClanBomber on frame buffer.
For X Window, just use plain legacy ClanBomber.

%prep
%setup -q
%patch0 -p1
%patch8 -p1 -b .peroyvind
%patch12 -p1 -b .x86_64

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=ClanBomber
Comment=Clanbomber - free (GPL) Bomberman-like multiplayer game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_gamesbindir}/*
%{_gamesdatadir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Fri Dec 17 2010 Funda Wang <fwang@mandriva.org> 0.9.1-13mdv2011.0
+ Revision: 622444
- rebuild for new directfb

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-12mdv2011.0
+ Revision: 610139
- rebuild

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 0.9.1-11mdv2010.1
+ Revision: 463329
- rebuild for new dfb

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-10mdv2010.0
+ Revision: 437032
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.9.1-9mdv2009.1
+ Revision: 350660
- rebuild

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 0.9.1-8mdv2009.0
+ Revision: 282228
- bunzip2 patch8
- adopt to fusionsound git api
- new license policy

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-7mdv2009.0
+ Revision: 266524
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 0.9.1-6mdv2009.0
+ Revision: 213229
- rebuild for new directfb

* Mon May 05 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-5mdv2009.0
+ Revision: 201406
- fix description (#38231)

* Tue Mar 04 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.1-4mdv2008.1
+ Revision: 178816
- revert obsolete of clanbomber (not a good idea according to tv)

* Tue Mar 04 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.1-3mdv2008.1
+ Revision: 178258
- provides and obsoletes clanbomber

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 132325
- drop old menu entry
- kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Thierry Vignaud <tv@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 98942
- new release
- rename spec file for consistency

* Sun Sep 02 2007 Crispin Boylan <crisb@mandriva.org> 0.9-6mdv2008.0
+ Revision: 78082
- Patch12: 64-bit fixes
- Patch11: fix compile against new fusion sound

  + Thierry Vignaud <tv@mandriva.org>
    - Import clanbomber2



* Mon Sep 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9-5mdv2007.0
- XDG

* Fri Feb 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9-4mdk
- rebuild for new directfb

* Tue May 10 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9-3mdk
- rebuild for new directfb

* Mon Aug 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9-2mdk
- rebuild for new g++
- patch 10: fix compiling with new g++
- fix build

* Tue May 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9-1mdk
- new release
- drop patch9

* Sat Apr 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.05-1mdk
- 0.5
- fix build when there's no $DISPLAY available (P9 from debian)
- fix buildrequires
- change summary macro to avoid conflicts if we were to build debug package
- spec cosmetics

* Wed Jan 21 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 1.04-1mdk
- new version (many patches including MANDRAKE_KEYS merged upstream ;p)

* Tue Sep  2 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-11mdk
- fix build deps for 64bit platform

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.02-10mdk
- rebuild
- convert icons to png
- fix missing header (P8)

* Mon Jan 20 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-9mdk
- rebuild for clanlib-0.6.x

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.02-8mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Mon Jul 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.02-7mdk
- Remove NO_XALF from menu entry

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-6mdk
- recompile against latest libstdc++ and latest clanlib

* Wed Feb 20 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-5mdk
- add patch #6 so that clanbomber can find its files

* Mon Nov 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-4mdk
- recompile against clanlib-0.5.1 (binary datafiles are not compatible
  with 0.5.0)

* Mon Oct 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-3mdk
- fix obsolete-tag Copyright
- fix URL

* Mon Sep 10 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-2mdk
- don't require launch_x11_clanapp
- use version 1.02a to fix an ugly memory leak
- fix music

* Fri May  4 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.02-1mdk
- 1.02 which is compliant with ClanLib-0.5

* Mon Apr  9 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.01-12mdk
- Fix menu entry for GNOME

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-11mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Fri Feb 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-10mdk
- add 48x48 icon
- fix requires on launch_x11_clanapp

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-9mdk
- rebuild to follow new lib policy of clanlib

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-8mdk
- recompile against newest libstdc++
- against lowercased hermes and clanlib

* Tue Oct 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-7mdk
- fix compile with gcc-2.96

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-6mdk
- menu: now launches automatically the x11 target

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-5mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.01-4mdk
- automatically added BuildRequires

* Tue Aug  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-3mdk
- menu entry

* Tue Aug  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-2mdk
- added patch for support for mandrake keys (use MANDRAKE_KEYS envvar)

* Mon Jul 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.01-1mdk
- first package for Linux-Mandrake
