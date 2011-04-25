%define name	gsetroot
%define version	1.1
%define release	1

Summary:	Gtk-based front-end for Esetroot
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://gsetroot.sf.net
BuildRequires:	gtk2-devel
Requires:	eterm

%description
Use it to configure root window under a Window Manager like FluxBox,
Enlightenment, WindowMaker, NextStep, BlackBox..

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}/usr/doc/* 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_bindir}/%{name}
