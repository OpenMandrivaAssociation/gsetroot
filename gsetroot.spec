%define name gsetroot
%define version 1.0
%define release  %mkrel 7

Summary: Gtk-based front-end for Esetroot
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://gsetroot.sf.net
BuildRequires: automake1.8 gtk2-devel
Requires: eterm

%description
Use it to configure root window under a Window Manager like FluxBox,
Enlightenment, WindowMaker, NextStep, BlackBox..

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%makeinstall
rm -rf $RPM_BUILD_ROOT/usr/doc/* 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}

