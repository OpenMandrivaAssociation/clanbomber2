Summary:	Clanbomber - free (GPL) Bomberman-like multiplayer game
Name:		clanbomber2
Version:	0.9.1
Release:	15
License:	GPLv2+
Group:		Games/Arcade
Url:		http://clanbomber.sourceforge.net/
Source0:	http://www.clanbomber.de/files/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		fusionsound_new_api.patch
Patch8:		clanbomber-1.02a-gcc-3.3.patch
Patch12:	clanbomber2-0.9-x86_64.patch
BuildRequires:	hermes-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libclanlib2-sound
BuildRequires:	pkgconfig(fusionsound)
BuildRequires:	pkgconfig(zlib)

%description
ClanBomber is a free (GPL) Bomberman-like multiplayer game that uses ClanLib, a
free multi platform C++ game SDK. First "ClanBomber" was only a working title
for a small game started in September 1998, that has only been started to learn
how to use ClanLib. But the ClanBomber project has grown into a real game. It
is fully playable and features Computer controlled bombers, however, it is
recommended to play ClanBomber with friends (3-8 players are really fun).

Clanbomber2 is a port of ClanBomber on frame buffer.
For X Window, just use plain legacy ClanBomber.

%files
%doc AUTHORS COPYING README
%{_gamesbindir}/*
%{_gamesdatadir}/*
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch8 -p1 -b .peroyvind
%patch12 -p1 -b .x86_64

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="%{optflags} -fno-omit-frame-pointer" CXXFLAGS="%{optflags} -fno-omit-frame-pointer"
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=ClanBomber
Comment=Clanbomber - free (GPL) Bomberman-like multiplayer game
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

