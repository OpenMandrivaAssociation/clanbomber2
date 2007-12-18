%define	name	clanbomber2
%define	version	0.9.1
%define	release	%mkrel 2
%define	Summary	Clanbomber - free (GPL) Bomberman-like multiplayer game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://www.clanbomber.de/files/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch8:		clanbomber-1.02a-gcc-3.3.patch.bz2
Patch12:	clanbomber2-0.9-x86_64.patch
URL:		http://clanbomber.sourceforge.net/
License:	GPL
Group:		Games/Arcade
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

%prep
%setup -q
%patch8 -p1 -b .peroyvind
%patch12 -p1 -b .x86_64
#perl -pi -e 's|\@datadir\@|\$(datadir)|' */Makefile.am */*/Makefile.am
#aclocal-1.7

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

%post
%{update_menus}

%postun
%{clean_menus}

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